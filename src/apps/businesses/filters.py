import django_filters

from apps.businesses.models import Business


class BusinessListCreateFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    locality_id = django_filters.NumberFilter()

    class Meta:
        model = Business
        fields = ["name", "locality_id"]
