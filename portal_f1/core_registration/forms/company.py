from django import forms
from core_registration.models.company import Company
from core_registration.models.city import City
from django.conf import settings
from core_access.models import User

class CompanyForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Descrição",
                "maxlength": 150,
                "class": "form-control"
            }
        ), required=True,
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Endereço",
                "maxlength": 200,
                "class": "form-control"
            }
        ), required=True,
    )
    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     widget=forms.widgets.Select(
    #         attrs={
    #             "placeholder": "User who registered the company",
    #             "class": "form-control"
    #         }
    #     ), required=True,
    # )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.widgets.Select(
            attrs={
                "placeholder": "Cidade",
                "class": "js-example-basic-single form-control needs-validation",
                "id": "city"
            }
        )
        , required=True,
    )

    class Meta:
        model = Company
        fields = ['description', 'address', 'city']