import django_filters
from django import forms
from django.db.models import Q
from core_registration.models.company import Company

class CompanyFilter(django_filters.FilterSet):
    filter_text = django_filters.CharFilter(
        method='filter_all',
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Filtrar todos",
                "maxlength": 10,
                "class": "form-control mx-sm-3",
                "id": "filter_company",
            }
        ), required=False,
    )
    def filter_all(self, queryset, name, value):
        return Company.objects.filter(
            Q(registration_date__icontains=value)|
            Q(description__icontains=value)|
            Q(address__icontains=value)|
            Q(user__username__icontains=value)|
            Q(city__description__icontains=value)
        )

    class Meta:
        model = Company
        fields = ['filter_text']