import django_filters
from django import forms
from django.db.models import Q
from core_access.models import User

class UserFilter(django_filters.FilterSet):
    filter_text = django_filters.CharFilter(
        method='filter_all',
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Filtrar todos",
                "maxlength": 10,
                "class": "form-control mx-sm-3",
                "id": "filter_user",
            }
        ), required=False,
    )
    def filter_all(self, queryset, name, value):
        return User.objects.filter(
            Q(username__icontains=value)|
            Q(first_name__icontains=value)|
            Q(last_name__icontains=value)|
            Q(email__icontains=value)
        )

    class Meta:
        model = User
        fields = ['filter_text']