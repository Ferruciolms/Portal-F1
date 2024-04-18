from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cpf = models.CharField(max_length=14, verbose_name='CPF', null=True, blank=True)
    telephone = models.CharField(max_length=15, verbose_name="Telephone", blank=True, null=True)
    email = models.CharField(max_length=50, verbose_name="e-mail", null=True, blank=True)
    login_disabled = models.BooleanField(default=False, verbose_name="User can't login")

    class Meta:
        ordering = ['id']

    def is_manager(self):
        return self.groups.filter(name='Administrador').exists() or self.is_superuser

    def is_validator(self):
        return self.groups.filter(name='Validador').exists() or self.is_superuser

    def is_observer(self):
        return self.groups.filter(name='Observador').exists() or self.is_superuser

    def __str__(self):
        return "{}".format(self.first_name)
