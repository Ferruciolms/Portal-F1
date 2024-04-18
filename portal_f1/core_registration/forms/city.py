from django import forms
from core_registration.models.city import City
from core_registration.models.state import State
from django.conf import settings
from core_access.models import User

class CityForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Descrição",
                "maxlength": 45,
                "class": "form-control"
            }
        ), required=True,
    )
    state = forms.ModelChoiceField(
        queryset=State.objects.all(),
        widget=forms.widgets.Select(
            attrs={
                "placeholder": "Estado",
                "class": "js-example-basic-single form-control needs-validation",
            }
        )
        , required=True,
    )

    class Meta:
        model = City
        fields = ['description', 'state']