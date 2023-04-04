from django.urls import path

from apps.businesses.views import (
    BusinessListCreate,
    BusinessAddressVerify,
    BusinessAmenityRetrieve,
    BusinessAmenityVerify,
    BusinessAmenityVerifyToBeTrue,
    BusinessAmenityVerifyToBeFalse,
    BusinessAmenitiesBulkVerify,
    BusinessRetrieve,
    LocalityList,
)


urlpatterns = [
    path("", BusinessListCreate.as_view(), name="list-create-businesses"),
    path(
        "<int:pk>/",
        BusinessRetrieve.as_view(),
        name="retrieve-business",
    ),
    path(
        "<int:pk>/address/verify/",
        BusinessAddressVerify.as_view(),
        name="verify-business-address",
    ),
    path(
        "<int:pk>/amenities/verify/",
        BusinessAmenitiesBulkVerify.as_view(),
        name="bulk-verify-business-amenities",
    ),
    path(
        "amenities/<int:pk>/",
        BusinessAmenityRetrieve.as_view(),
        name="retrieve-business-amenity",
    ),
    path(
        "amenities/<int:pk>/verify/",
        BusinessAmenityVerify.as_view(),
        name="verify-business-amenity",
    ),
    path(
        "amenities/<int:pk>/verify/to-be-true/",
        BusinessAmenityVerifyToBeTrue.as_view(),
        name="verify-business-amenity-to-be-true",
    ),
    path(
        "amenities/<int:pk>/verify/to-be-false/",
        BusinessAmenityVerifyToBeFalse.as_view(),
        name="verify-business-amenity-to-be-false",
    ),
    path(
        "localities/",
        LocalityList.as_view(),
        name="list-localities",
    ),
]
