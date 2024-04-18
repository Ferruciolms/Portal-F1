import django_filters
from django import forms
from django.db.models import Q
from core_registration.models.country import Country

class CountryFilter(django_filters.FilterSet):
    filter_text = django_filters.CharFilter(
        method='filter_all',
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Filtrar todos",
                "maxlength": 10,
                "class": "form-control mx-sm-3",
                "id": "filter_country",
            }
        ), required=False,
    )
    def filter_all(self, queryset, name, value):
        return Country.objects.filter(
            Q(id__icontains=value)|
            Q(description__icontains=value)
        )

    class Meta:
        model = Country
        fields = ['filter_text']