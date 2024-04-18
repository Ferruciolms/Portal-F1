from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from core_access.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, Group
from localflavor.br.forms import BRCPFField
from core_access.validators.password_register_validator import Password_Register_Validator
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


# usuário altera seu cadastro
class ProfileLoggedForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "maxlength": 30,
                "class": "form-control"
            }
        ), required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "maxlength": 150,
                "class": "form-control"
            }
        ), required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-mail",
                "class": "form-control"
            }
        )
    )
    cpf = BRCPFField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "CPF",
                "class": "form-control",
                "data-mask": "000.000.000-00"
            }
        ), required=False,
    )
    telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone",
                "maxlength": 11,
                "class": "form-control",
                "data-mask": "(00) 00000-0000"
            }
        ), required=True,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'cpf', 'telephone']


# editar cadastro de usuário - ADM
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "maxlength": 30,
                "class": "form-control"
            }
        ), required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "maxlength": 150,
                "class": "form-control",
            }
        ), required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-mail",
                "class": "form-control"
            }
        )
    )
    cpf = BRCPFField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "CPF",
                "class": "form-control",
                "data-mask": "000.000.000-00"
            }
        ), required=False,
    )
    telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone",
                "class": "form-control",
                "data-mask": "(00) 00000-0000",

            }
        ), required=True,
    )
    CHOICES = ((True, "Ativo"), (False, "Inativo"))
    is_active= forms.ChoiceField(
        choices=CHOICES,
        widget=forms.widgets.Select(
            attrs={
                "class": "form-control"
            }
        ), required=False,
    )

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.widgets.Select(
            attrs={
                "class": "form-control"
            }
        ), required=True,
    )


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'cpf', 'telephone', 'is_active', 'group']



class AccountChangeForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-mail",
                "class": "form-control"
            }
        )
    )
    cpf = BRCPFField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "CPF",
                "class": "form-control",
                "data-mask": "000.000.000-00"
            }
        ), required=False,
    )
    telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone",
                "class": "form-control",
                "data-mask": "(00) 00000-0000",

            }
        ), required=True,
    )
    class Meta(UserChangeForm.Meta):
        model = User


class AccountPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha antiga",
                "class": "form-control"
            }
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Nova senha",
                "class": "form-control"
            }
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmar senha",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1')


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Usuário",
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Senha",
                "class": "form-control"
            }
        )
    )

    # captcha = ReCaptchaField(
    #     widget=ReCaptchaV2Invisible()
    # )

class Password_ResetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "maxlength": 30,
                "class": "form-control"
            }
        ), required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "maxlength": 150,
                "class": "form-control",
            }
        ), required=True,
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuário",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Senha",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirmar Senha",
                "class": "form-control"
            }
        ),
        validators=[
            Password_Register_Validator().validate_min_length_password,
            Password_Register_Validator().validate_upper_case,
            Password_Register_Validator().validate_number_case,
        ]
    )

# Cadastrar novo usuário - ADM
class AccountCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Usuário",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "E-mail",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Senha",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Repita a senha",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "maxlength": 30,
                "class": "form-control"
            }
        ), required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "maxlength": 150,
                "class": "form-control"
            }
        ), required=True,
    )
    cpf = BRCPFField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "CPF",
                "class": "form-control",
                "data-mask": "000.000.000-00"
            }
        ), required=False,
    )
    telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone",
                "maxlength": 11,
                "class": "form-control",
                "data-mask": "(00) 00000-0000",
            }
        ), required=True,
    )

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.widgets.Select(
            attrs={
                "class": "form-control"
            }
        ), required=True,
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                  'cpf', 'telephone', 'group']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("O email {} já esta cadastrado.".format(email))

        return email

