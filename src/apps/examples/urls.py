from django.urls import path

from apps.examples.views import ExampleList


urlpatterns = [
    path("", ExampleList.as_view(), name="list-examples"),
]
