from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.businesses.filters import BusinessListCreateFilter
from apps.businesses.models import Business, BusinessAmenity, Locality
from apps.businesses.serializers import (
    BusinessSerializer,
    BusinessAmenitySerializer,
    LocalitySerializer,
)


class LocalityList(ListAPIView):
    serializer_class = LocalitySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Locality.objects.all()


class BusinessListCreate(ListCreateAPIView):
    serializer_class = BusinessSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BusinessListCreateFilter
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Business.objects.all()


class BusinessRetrieve(RetrieveAPIView):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        return Business.objects.all()


class BusinessAddressVerify(APIView):
    def patch(self, request, *args, **kwargs):
        business = Business.objects.get(id=kwargs["pk"])
        business.formatted_address_last_verified_at = timezone.now()
        business.save(update_fields=["formatted_address_last_verified_at"])
        serializer = BusinessSerializer(business, many=False, read_only=True)
        return Response(serializer.data)


class BusinessAmenityRetrieve(RetrieveAPIView):
    serializer_class = BusinessAmenitySerializer

    def get_queryset(self):
        return BusinessAmenity.objects.all()


class BusinessAmenityVerifyToBeTrue(APIView):
    def patch(self, request, *args, **kwargs):
        business_amenity = BusinessAmenity.objects.get(id=kwargs["pk"])
        business_amenity.is_supported = True
        business_amenity.last_verified_at = timezone.now()
        business_amenity.save(
            update_fields=["last_verified_at", "is_supported", "updated_at"]
        )
        serializer = BusinessAmenitySerializer(
            business_amenity, many=False, read_only=True
        )
        return Response(serializer.data)


class BusinessAmenityVerifyToBeFalse(APIView):
    def patch(self, request, *args, **kwargs):
        business_amenity = BusinessAmenity.objects.get(id=kwargs["pk"])
        business_amenity.is_supported = False
        business_amenity.last_verified_at = timezone.now()
        business_amenity.save(
            update_fields=["last_verified_at", "is_supported", "updated_at"]
        )
        serializer = BusinessAmenitySerializer(
            business_amenity, many=False, read_only=True
        )
        return Response(serializer.data)


class BusinessAmenityVerify(APIView):
    def patch(self, request, *args, **kwargs):
        business_amenity = BusinessAmenity.objects.get(id=kwargs["pk"])
        business_amenity.last_verified_at = timezone.now()
        business_amenity.save(update_fields=["last_verified_at"])
        serializer = BusinessAmenitySerializer(
            business_amenity, many=False, read_only=True
        )
        return Response(serializer.data)


class BusinessAmenitiesBulkVerify(APIView):
    def patch(self, request, *args, **kwargs):
        BusinessAmenity.objects.filter(business_id=kwargs["pk"]).exclude(
            is_supported=None
        ).update(last_verified_at=timezone.now())

        business = Business.objects.get(id=kwargs["pk"])
        serializer = BusinessSerializer(business, many=False, read_only=True)
        return Response(serializer.data)
