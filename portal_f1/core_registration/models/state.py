from django.db import models
from core_registration.models.country import Country


class State(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    description = models.CharField(max_length=100, verbose_name='Descrição', null=False)
    acronym = models.CharField(max_length=2, verbose_name='Sigla', null=False)
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.PROTECT, null=False)
    is_deleted = models.BooleanField(verbose_name="Is Deleted?", null=False, blank=False, default=False)

    class Meta:
        verbose_name_plural = "States"
        ordering = ['-id']

    def __str__(self):
        return "{} - {}".format(self.acronym, self.description)