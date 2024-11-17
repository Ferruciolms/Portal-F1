import django_filters
from django import forms
from django.db.models import Q
from analytics.models.circuits import Circuit


class CircuitFilter(django_filters.FilterSet):
    filter_text = django_filters.CharFilter(
        method='filter_all',
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Filter All",
                "maxlength": 100,
                "class": "form-control mx-sm-3",
                "id": "filter_circuit",
            }
        ), required=False,
    )

    def filter_all(self, queryset, name, value):
        return Circuit.objects.filter(
            Q(name__icontains=value) |
            Q(city__icontains=value) |
            Q(country__icontains=value)

        )

    class Meta:
        model = Circuit
        fields = ['filter_text']