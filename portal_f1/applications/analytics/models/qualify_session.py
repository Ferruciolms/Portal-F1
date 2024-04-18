from django.db import models
from analytics.models.races import Race


class QualifySession(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Qualify ID", blank=False, null=False)
    date = models.DateField(verbose_name="Qualify Date", null=False, blank=False)
    time = models.TimeField(verbose_name="Qualify Time", null=False, blank=True)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Race Id", blank=False, null=False)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = "Qualify Sessions"
