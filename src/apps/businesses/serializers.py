from django.utils import timezone
from rest_framework import serializers, validators

from apps.businesses.models import (
    AmenityType,
    Business,
    BusinessAmenity,
    Locality,
    Neighborhood,
    PostalCode,
    State,
)
from apps.businesses.utils import get_elapsed_time


class PostalCodeSerializer(serializers.ModelSerializer):
    value = serializers.CharField(
        max_length=5,
        allow_blank=True,
        write_only=True,
    )
    readable_value = serializers.CharField(source="value", read_only=True)

    class Meta:
        model = PostalCode
        fields = ("id", "value", "readable_value")


class NeighborhoodSerializer(serializers.ModelSerializer):
    value = serializers.CharField(
        max_length=50,
        allow_blank=True,
        write_only=True,
    )
    readable_value = serializers.CharField(source="value", read_only=True)

    class Meta:
        model = Neighborhood
        fields = ("id", "value", "readable_value")


class LocalitySerializer(serializers.ModelSerializer):
    value = serializers.CharField(
        max_length=50,
        allow_blank=True,
        write_only=True,
    )
    readable_value = serializers.CharField(source="value", read_only=True)

    class Meta:
        model = Locality
        fields = ("id", "value", "readable_value")


class StateSerializer(serializers.ModelSerializer):
    value = serializers.CharField(
        max_length=2,
        allow_blank=True,
        write_only=True,
    )
    readable_value = serializers.CharField(source="value", read_only=True)

    class Meta:
        model = State
        fields = ("id", "value", "readable_value")


class BusinessAmenitySerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=50, write_only=True)
    readable_type = serializers.CharField(source="get_type_display", read_only=True)
    is_supported = serializers.BooleanField()
    readable_is_supported = serializers.SerializerMethodField()
    last_verified_at = serializers.DateTimeField(required=False, write_only=True)
    last_verified_at_elapsed_time = serializers.SerializerMethodField()

    class Meta:
        model = BusinessAmenity
        fields = (
            "id",
            "type",
            "readable_type",
            "is_supported",
            "readable_is_supported",
            "last_verified_at",
            "last_verified_at_elapsed_time",
        )

    def get_readable_is_supported(self, instance):
        match instance.is_supported:
            case True:
                return "Yes"
            case False:
                return "No"
            case _:
                return "Undefined"

    def get_last_verified_at_elapsed_time(self, instance):
        if not instance.last_verified_at:
            return None

        return get_elapsed_time(instance.last_verified_at)


class BusinessSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    google_id = serializers.CharField(
        max_length=50,
        validators=[validators.UniqueValidator(queryset=Business.objects.all())],
    )
    formatted_address = serializers.CharField(max_length=255)
    postal_code = PostalCodeSerializer(many=False)
    neighborhood = NeighborhoodSerializer(many=False)
    locality = LocalitySerializer(many=False)
    state = StateSerializer(many=False)
    amenities = BusinessAmenitySerializer(many=True, read_only=True)
    supported_amenities = serializers.SerializerMethodField()
    formatted_address_last_verified_at = serializers.DateTimeField(
        required=False, write_only=True
    )
    formatted_address_last_verified_at_elapsed_time = (
        serializers.SerializerMethodField()
    )

    class Meta:
        model = Business
        fields = (
            "id",
            "name",
            "google_id",
            "formatted_address",
            "postal_code",
            "neighborhood",
            "locality",
            "state",
            "amenities",
            "supported_amenities",
            "formatted_address_last_verified_at",
            "formatted_address_last_verified_at_elapsed_time",
        )

    def create(self, validated_data):
        postal_code_data = validated_data.pop("postal_code")
        neighborhood_data = validated_data.pop("neighborhood")
        locality_data = validated_data.pop("locality")
        state_data = validated_data.pop("state")
        postal_code, _ = PostalCode.objects.update_or_create(**postal_code_data)
        neighborhood, _ = Neighborhood.objects.update_or_create(**neighborhood_data)
        locality, _ = Locality.objects.update_or_create(**locality_data)
        state, _ = State.objects.update_or_create(**state_data)

        business = Business.objects.create(
            postal_code=postal_code,
            neighborhood=neighborhood,
            locality=locality,
            state=state,
            formatted_address_last_verified_at=timezone.now(),
            **validated_data,
        )

        amenities = []
        for amenity_type in AmenityType.values:
            amenities.append(BusinessAmenity(business=business, type=amenity_type))
        BusinessAmenity.objects.bulk_create(amenities)

        return business

    def get_formatted_address_last_verified_at_elapsed_time(self, instance):
        return get_elapsed_time(instance.formatted_address_last_verified_at)

    def get_supported_amenities(self, instance):
        return BusinessAmenitySerializer(
            instance.amenities.filter(is_supported=True), many=True, read_only=True
        ).data
