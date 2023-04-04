import pytest
from datetime import datetime, timedelta
from django.urls import reverse
from django.utils import timezone


class TestBusinessListCreate:
    url = reverse("list-create-businesses")

    @pytest.mark.django_db
    def test_get(self, api_client, business_factory):
        expected = [
            {
                "id": 1,
                "name": "Scenic Brewery",
                "google_id": "xyz",
                "formatted_address": "1000 California Ln, San Diego, CA 92037, USA",
                "postal_code": {"id": 1, "readable_value": "92037"},
                "neighborhood": None,
                "locality": {"id": 4, "readable_value": "San Diego"},
                "state": {"id": 2, "readable_value": "CA"},
                "amenities": [],
                "supported_amenities": [],
                "formatted_address_last_verified_at_elapsed_time": "Less than a minute ago",
            },
        ]

        business_factory(
            name="Scenic Brewery",
            google_id="xyz",
            formatted_address="1000 California Ln, San Diego, CA 92037, USA",
            postal_code__value="92037",
            locality__value="San Diego",
            state__value="CA",
        )

        response = api_client.get(self.url)

        assert response.status_code == 200
        assert response.data == expected

    @pytest.mark.django_db
    def test_post(self, api_client):
        expected = {
            "id": 1,
            "name": "Scenic Brewery",
            "google_id": "xyz",
            "formatted_address": "1000 California Ln, San Diego, CA 92037, USA",
            "postal_code": {"id": 1, "readable_value": "92037"},
            "neighborhood": {"id": 1, "readable_value": "La Jolla"},
            "locality": {"id": 4, "readable_value": "San Diego"},
            "state": {"id": 2, "readable_value": "CA"},
            "amenities": [
                {
                    "id": 1,
                    "readable_type": "Serves Coffee",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 2,
                    "readable_type": "Serves Food",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 3,
                    "readable_type": "Serves Beer",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 4,
                    "readable_type": "Serves Wine",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 5,
                    "readable_type": "Serves Liquor",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 6,
                    "readable_type": "Is Takeout Only",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 7,
                    "readable_type": "Allows Laptops",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 8,
                    "readable_type": "Has Wifi",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 9,
                    "readable_type": "Has Tv",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 10,
                    "readable_type": "Can Play Sound",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
            ],
            "supported_amenities": [],
            "formatted_address_last_verified_at_elapsed_time": "Less than a minute ago",
        }

        data = {
            "name": "Scenic Brewery",
            "google_id": "xyz",
            "formatted_address": "1000 California Ln, San Diego, CA 92037, USA",
            "postal_code": {"value": "92037"},
            "neighborhood": {"value": "La Jolla"},
            "locality": {"value": "San Diego"},
            "state": {"value": "CA"},
        }
        response = api_client.post(self.url, data, format="json")

        assert response.status_code == 201
        assert response.data == expected


class TestBusinessRetrieve:
    @pytest.mark.django_db
    def test_get(self, api_client, business_factory):
        expected = {
            "id": 1,
            "name": "Scenic Brewery",
            "google_id": "xyz",
            "formatted_address": "1000 California Ln, San Diego, CA 92037, USA",
            "postal_code": {"id": 1, "readable_value": "92037"},
            "neighborhood": None,
            "locality": {"id": 4, "readable_value": "San Diego"},
            "state": {"id": 2, "readable_value": "CA"},
            "amenities": [],
            "supported_amenities": [],
            "formatted_address_last_verified_at_elapsed_time": "Less than a minute ago",
        }

        business_factory(
            name="Scenic Brewery",
            google_id="xyz",
            formatted_address="1000 California Ln, San Diego, CA 92037, USA",
            postal_code__value="92037",
            locality__value="San Diego",
            state__value="CA",
        )

        url = reverse("retrieve-business", kwargs={"pk": 1})
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data == expected


class TestBusinessAddressVerify:
    @pytest.mark.django_db
    def test_patch(self, api_client, business_factory):
        expected = {
            "id": 1,
            "name": "Scenic Brewery",
            "google_id": "xyz",
            "formatted_address": "1000 California Ln, San Diego, CA 92037, USA",
            "postal_code": {"id": 1, "readable_value": "92037"},
            "neighborhood": None,
            "locality": {"id": 4, "readable_value": "San Diego"},
            "state": {"id": 2, "readable_value": "CA"},
            "amenities": [],
            "supported_amenities": [],
            "formatted_address_last_verified_at_elapsed_time": "Less than a minute ago",
        }

        business_factory(
            name="Scenic Brewery",
            google_id="xyz",
            formatted_address="1000 California Ln, San Diego, CA 92037, USA",
            formatted_address_last_verified_at=timezone.make_aware(
                datetime.today() - timedelta(days=1)
            ),
            postal_code__value="92037",
            locality__value="San Diego",
            state__value="CA",
        )

        url = reverse("verify-business-address", kwargs={"pk": 1})
        response = api_client.patch(url, format="json")

        assert response.status_code == 200
        assert response.data == expected


@pytest.mark.parametrize(
    "is_supported,readable_is_supported,last_verified_at,last_verified_at_elapsed_time",
    [
        (None, "Undefined", None, None),
        (True, "Yes", timezone.now(), "Less than a minute ago"),
        (False, "No", timezone.now(), "Less than a minute ago"),
    ],
)
class TestBusinessAmenityRetrieve:
    @pytest.mark.django_db
    def test_get(
        self,
        api_client,
        business_amenity_factory,
        is_supported,
        readable_is_supported,
        last_verified_at,
        last_verified_at_elapsed_time,
    ):
        expected = {
            "id": 1,
            "readable_type": "Serves Coffee",
            "is_supported": is_supported,
            "readable_is_supported": readable_is_supported,
            "last_verified_at_elapsed_time": last_verified_at_elapsed_time,
        }

        business_amenity_factory(
            is_supported=is_supported, last_verified_at=last_verified_at
        )

        url = reverse("retrieve-business-amenity", kwargs={"pk": 1})
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data == expected


class TestBusinessAmenityVerifyToBeTrue:
    @pytest.mark.django_db
    def test_patch(self, api_client, business_amenity_factory):
        expected = {
            "id": 1,
            "readable_type": "Serves Coffee",
            "is_supported": True,
            "readable_is_supported": "Yes",
            "last_verified_at_elapsed_time": "Less than a minute ago",
        }

        business_amenity_factory(is_supported=None)

        url = reverse("verify-business-amenity-to-be-true", kwargs={"pk": 1})
        response = api_client.patch(url, format="json")

        assert response.status_code == 200
        assert response.data == expected


class TestBusinessAmenityVerifyToBeFalse:
    @pytest.mark.django_db
    def test_patch(self, api_client, business_amenity_factory):
        expected = {
            "id": 1,
            "readable_type": "Serves Coffee",
            "is_supported": False,
            "readable_is_supported": "No",
            "last_verified_at_elapsed_time": "Less than a minute ago",
        }

        business_amenity_factory(is_supported=None)

        url = reverse("verify-business-amenity-to-be-false", kwargs={"pk": 1})
        response = api_client.patch(url, format="json")

        assert response.status_code == 200
        assert response.data == expected


class TestBusinessAmenityVerify:
    @pytest.mark.django_db
    def test_patch(self, api_client, business_amenity_factory):
        expected = {
            "id": 1,
            "readable_type": "Serves Coffee",
            "is_supported": True,
            "readable_is_supported": "Yes",
            "last_verified_at_elapsed_time": "Less than a minute ago",
        }

        business_amenity_factory(
            is_supported=True,
            last_verified_at=timezone.make_aware(datetime.today() - timedelta(days=1)),
        )

        url = reverse("verify-business-amenity", kwargs={"pk": 1})
        response = api_client.patch(url, format="json")

        assert response.status_code == 200
        assert response.data == expected


class TestBusinessAmenitiesBulkVerify:
    @pytest.mark.django_db
    def test_patch(self, api_client, business_factory, business_amenity_factory):
        expected = {
            "id": 1,
            "name": "Scenic Brewery",
            "google_id": "xyz",
            "formatted_address": "1000 California Ln, San Diego, CA 92037, USA",
            "postal_code": {"id": 1, "readable_value": "92037"},
            "neighborhood": None,
            "locality": {"id": 4, "readable_value": "San Diego"},
            "state": {"id": 2, "readable_value": "CA"},
            "amenities": [
                {
                    "id": 1,
                    "readable_type": "Serves Coffee",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 2,
                    "readable_type": "Serves Food",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 3,
                    "readable_type": "Serves Beer",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 4,
                    "readable_type": "Serves Wine",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
                {
                    "id": 5,
                    "readable_type": "Serves Liquor",
                    "is_supported": False,
                    "readable_is_supported": "No",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 6,
                    "readable_type": "Is Takeout Only",
                    "is_supported": False,
                    "readable_is_supported": "No",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 7,
                    "readable_type": "Allows Laptops",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 8,
                    "readable_type": "Has Wifi",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 9,
                    "readable_type": "Has Tv",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 10,
                    "readable_type": "Can Play Sound",
                    "is_supported": None,
                    "readable_is_supported": "Undefined",
                    "last_verified_at_elapsed_time": None,
                },
            ],
            "supported_amenities": [
                {
                    "id": 1,
                    "readable_type": "Serves Coffee",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 2,
                    "readable_type": "Serves Food",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 3,
                    "readable_type": "Serves Beer",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 7,
                    "readable_type": "Allows Laptops",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 8,
                    "readable_type": "Has Wifi",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
                {
                    "id": 9,
                    "readable_type": "Has Tv",
                    "is_supported": True,
                    "readable_is_supported": "Yes",
                    "last_verified_at_elapsed_time": "Less than a minute ago",
                },
            ],
            "formatted_address_last_verified_at_elapsed_time": "1d ago",
        }

        business = business_factory(
            name="Scenic Brewery",
            google_id="xyz",
            formatted_address="1000 California Ln, San Diego, CA 92037, USA",
            formatted_address_last_verified_at=timezone.make_aware(
                datetime.today() - timedelta(days=1)
            ),
            postal_code__value="92037",
            locality__value="San Diego",
            state__value="CA",
        )
        business_amenity_factory(
            business=business,
            type="serves_coffee",
            is_supported=True,
            last_verified_at=timezone.make_aware(datetime.today() - timedelta(days=4)),
        )
        business_amenity_factory(
            business=business,
            type="serves_food",
            is_supported=True,
            last_verified_at=timezone.make_aware(datetime.today() - timedelta(hours=2)),
        )
        business_amenity_factory(
            business=business,
            type="serves_beer",
            is_supported=True,
            last_verified_at=timezone.make_aware(
                datetime.today() - timedelta(minutes=10)
            ),
        )
        business_amenity_factory(
            business=business,
            type="serves_wine",
            is_supported=None,
            last_verified_at=None,
        )
        business_amenity_factory(
            business=business,
            type="serves_liquor",
            is_supported=False,
            last_verified_at=timezone.make_aware(datetime.today() - timedelta(days=2)),
        )
        business_amenity_factory(
            business=business,
            type="is_takeout_only",
            is_supported=False,
            last_verified_at=timezone.make_aware(datetime.today() - timedelta(hours=5)),
        )
        business_amenity_factory(
            business=business,
            type="allows_laptops",
            is_supported=True,
            last_verified_at=timezone.make_aware(datetime.today() - timedelta(days=3)),
        )
        business_amenity_factory(
            business=business,
            type="has_wifi",
            is_supported=True,
            last_verified_at=timezone.make_aware(
                datetime.today() - timedelta(minutes=30)
            ),
        )
        business_amenity_factory(
            business=business,
            type="has_tv",
            is_supported=True,
            last_verified_at=timezone.make_aware(datetime.today() - timedelta(days=15)),
        )
        business_amenity_factory(
            business=business,
            type="can_play_sound",
            is_supported=None,
            last_verified_at=None,
        )

        url = reverse("bulk-verify-business-amenities", kwargs={"pk": 1})
        response = api_client.patch(url, format="json")

        assert response.status_code == 200
        assert response.data == expected


class TestLocalityList:
    @pytest.mark.django_db
    def test_get(self, api_client):
        expected = [
            {"id": 1, "readable_value": "New York"},
            {"id": 2, "readable_value": "Queens"},
            {"id": 3, "readable_value": "Brooklyn"},
        ]

        url = reverse("list-localities")
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data == expected
