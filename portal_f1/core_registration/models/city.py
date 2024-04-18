from django.db import models
from core_registration.models.state import State


class City(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    description = models.CharField(max_length=45, verbose_name='Description', null=False)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=False)
    is_deleted = models.BooleanField(verbose_name="Is Deleted?", null=False, blank=False, default=False)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['description']

    def __str__(self):
        return "{}".format(self.description)