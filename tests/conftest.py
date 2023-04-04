import factory
import pytest
import pytest_factoryboy
from faker import Faker
from rest_framework.test import APIClient

from apps.examples.models import Example

fake = Faker()


@pytest.fixture
def api_client():
    return APIClient()


@pytest_factoryboy.register
class ExampleFactory(factory.django.DjangoModelFactory):
    value = factory.LazyAttribute(lambda x: fake.pystr())

    class Meta:
        model = Example
