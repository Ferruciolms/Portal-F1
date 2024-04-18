import django_filters
from django import forms
from django.db.models import Q
from core_registration.models.city import City

class CityFilter(django_filters.FilterSet):
    filter_text = django_filters.CharFilter(
        method='filter_all',
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Filtrar todos",
                "maxlength": 10,
                "class": "form-control mx-sm-3",
                "id": "filter_city",
            }
        ), required=False,
    )
    def filter_all(self, queryset, name, value):
        return City.objects.filter(
            Q(id__icontains=value)|
            Q(description__icontains=value)|
            Q(state__description__icontains=value)
        )

    class Meta:
        model = City
        fields = ['filter_text']