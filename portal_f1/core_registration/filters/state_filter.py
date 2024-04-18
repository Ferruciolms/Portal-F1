import django_filters
from django import forms
from django.db.models import Q
from core_registration.models.state import State

class StateFilter(django_filters.FilterSet):
    filter_text = django_filters.CharFilter(
        method='filter_all',
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Filtrar todos",
                "maxlength": 10,
                "class": "form-control mx-sm-3",
                "id": "filter_state",
            }
        ), required=False,
    )
    def filter_all(self, queryset, name, value):
        return State.objects.filter(
            Q(id__icontains=value)|
            Q(description__icontains=value)|
            Q(acronym__icontains=value)|
            Q(country__description__icontains=value)
        )

    class Meta:
        model = State
        fields = ['filter_text']