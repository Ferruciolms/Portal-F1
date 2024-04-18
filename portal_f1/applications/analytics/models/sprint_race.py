from django.db import models
from analytics.models.races import Race


class SprintRace(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Sprint Race ID", blank=False, null=False)
    date = models.DateField(verbose_name="Sprint Date", null=False, blank=False)
    time = models.TimeField(verbose_name="Sprint Time", null=False, blank=True)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Race Id", blank=False, null=False)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = "Sprint Races"