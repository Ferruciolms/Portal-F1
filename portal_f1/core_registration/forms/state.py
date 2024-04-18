from django import forms
from core_registration.models.country import Country
from core_registration.models.state import State
from django.conf import settings
from core_access.models import User

class StateForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Descrição",
                "maxlength": 100,
                "class": "form-control"
            }
        ), required=True,
    )
    acronym = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sigla",
                "maxlength": 2,
                "class": "form-control"
            }
        ), required=True,
    )
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.widgets.Select(
            attrs={
                "placeholder": "País",
                "class": "form-control col-md-7"
            }
        )
        , required=True,
    )

    class Meta:
        model = State
        fields = ['description', 'acronym', 'country']