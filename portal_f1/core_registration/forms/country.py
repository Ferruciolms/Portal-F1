from django import forms
from core_registration.models.country import Country
from django.conf import settings
from core_access.models import User

class CountryForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Descrição",
                "maxlength": 100,
                "class": "form-control"
            }
        ), required=True,
    )

    class Meta:
        model = Country
        fields = ['description']