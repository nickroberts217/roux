from django.contrib import admin

from apps.businesses.models import (
    Business,
    BusinessAmenity,
    Locality,
    Neighborhood,
    PostalCode,
    State,
)


admin.site.register(Business)
admin.site.register(BusinessAmenity)
admin.site.register(Locality)
admin.site.register(Neighborhood)
admin.site.register(PostalCode)
admin.site.register(State)
