from django.db import models


class PostalCode(models.Model):
    value = models.CharField(max_length=5, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "postal codes"

    def __str__(self):
        return self.value


class Neighborhood(models.Model):
    value = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "neighborhoods"

    def __str__(self):
        return self.value


class Locality(models.Model):
    value = models.CharField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "localities"

    def __str__(self):
        return self.value


class State(models.Model):
    value = models.CharField(max_length=2, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "states"

    def __str__(self):
        return self.value


class AmenityType(models.TextChoices):
    SERVES_COFFEE = "serves_coffee"
    SERVES_FOOD = "serves_food"
    SERVES_BEER = "serves_beer"
    SERVES_WINE = "serves_wine"
    SERVES_LIQUOR = "serves_liquor"
    IS_TAKEOUT_ONLY = "is_takeout_only"
    ALLOWS_LAPTOPS = "allows_laptops"
    HAS_WIFI = "has_wifi"
    HAS_TV = "has_tv"
    CAN_PLAY_SOUND = "can_play_sound"


class Business(models.Model):
    name = models.CharField(max_length=100)
    google_id = models.CharField(max_length=50, unique=True)
    formatted_address = models.CharField(max_length=255)
    formatted_address_last_verified_at = models.DateTimeField()
    postal_code = models.ForeignKey(
        PostalCode, on_delete=models.SET_NULL, related_name="businesses", null=True
    )
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.SET_NULL, related_name="businesses", null=True
    )
    locality = models.ForeignKey(
        Locality, on_delete=models.SET_NULL, related_name="businesses", null=True
    )
    state = models.ForeignKey(
        State, on_delete=models.SET_NULL, related_name="businesses", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "businesses"

    def __str__(self):
        return self.name


class BusinessAmenity(models.Model):
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="amenities"
    )
    type = models.CharField(choices=AmenityType.choices, max_length=50)
    is_supported = models.BooleanField(null=True)
    last_verified_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "business amenities"

    def __str__(self):
        return f"{self.business}: {self.type}"
