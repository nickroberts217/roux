from rest_framework import serializers

from apps.examples.models import Example


class ExampleSerializer(serializers.ModelSerializer):
    value = serializers.CharField(max_length=50)

    class Meta:
        model = Example
        fields = ("id", "value")
