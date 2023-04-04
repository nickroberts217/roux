import factory
import pytest
import pytest_factoryboy
from django.utils import timezone
from faker import Faker
from rest_framework.test import APIClient

from apps.businesses.models import (
    Business,
    BusinessAmenity,
    Locality,
    PostalCode,
    State,
)

fake = Faker()


@pytest.fixture
def api_client():
    return APIClient()


@pytest_factoryboy.register
class PostalCodeFactory(factory.django.DjangoModelFactory):
    value = factory.LazyAttribute(lambda x: fake.postalcode())

    class Meta:
        model = PostalCode


@pytest_factoryboy.register
class LocalityFactory(factory.django.DjangoModelFactory):
    value = factory.LazyAttribute(lambda x: fake.city())

    class Meta:
        model = Locality


@pytest_factoryboy.register
class StateFactory(factory.django.DjangoModelFactory):
    value = factory.LazyAttribute(lambda x: fake.state_abbr())

    class Meta:
        model = State


@pytest_factoryboy.register
class BusinessFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: " ".join(fake.words()))
    google_id = factory.LazyAttribute(lambda x: fake.pystr())
    formatted_address = factory.LazyAttribute(lambda x: fake.address())
    formatted_address_last_verified_at = timezone.now()
    postal_code = factory.SubFactory(PostalCodeFactory)
    locality = factory.SubFactory(LocalityFactory)
    state = factory.SubFactory(StateFactory)

    class Meta:
        model = Business


@pytest_factoryboy.register
class BusinessAmenityFactory(factory.django.DjangoModelFactory):
    business = factory.SubFactory(BusinessFactory)
    type = "serves_coffee"

    class Meta:
        model = BusinessAmenity
