from rest_framework.generics import ListAPIView

from apps.examples.models import Example
from apps.examples.serializers import ExampleSerializer


class ExampleList(ListAPIView):
    serializer_class = ExampleSerializer

    def get_queryset(self):
        return Example.objects.all()
