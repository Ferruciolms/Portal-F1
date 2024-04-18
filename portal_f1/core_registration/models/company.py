from django.db import models
from django.contrib.auth.models import User
from core_registration.models.city import City
from django.conf import settings


class Company(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Registration date')
    description = models.CharField(max_length=150, verbose_name='Description', null=False, blank=False)
    address = models.CharField(max_length=200, verbose_name='Address', null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                             verbose_name='User who registered the company ', null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='City', null=False, blank=False)
    is_deleted = models.BooleanField(verbose_name="Is Deleted?", null=False, blank=False, default=False)

    # campo_foreig = models.ForeignKey(NomeClasse, on_delete=models.PROTECT)
    def __str__(self):
        return "{}".format(self.description)

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['-id']