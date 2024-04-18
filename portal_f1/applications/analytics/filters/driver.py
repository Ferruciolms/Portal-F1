import django_filters
from django import forms
from django.db.models import Q
from analytics.models.drivers import Driver


class DriverFilter(django_filters.FilterSet):
    filter_text = django_filters.CharFilter(
        method='filter_all',
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Filter All",
                "maxlength": 20,
                "class": "form-control mx-sm-3",
                "id": "filter_driver",
            }
        ), required=False,
    )

    def filter_all(self, queryset, name, value):
        return Driver.objects.filter(
            Q(fname__icontains=value) |
            Q(lname__icontains=value)
        )

    class Meta:
        model = Driver
        fields = ['filter_text']