import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_list(api_client, example_factory):
    example_factory(value="testing")
    expected = [{"id": 1, "value": "testing"}]

    url = reverse("list-examples")
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data == expected
