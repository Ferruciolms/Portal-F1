from django.db import models
from analytics.models.results import Result


class FastestLap(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Fastest Lap ID", blank=False, null=False)
    lap = models.IntegerField(verbose_name="Lap", blank=False, null=False)
    rank = models.IntegerField(verbose_name="Rank Fastest Lap", blank=False, null=False)
    time = models.TimeField(verbose_name="Time Lap", blank=False, null=False)
    speed = models.FloatField(verbose_name="Speed lap", blank=False, null=False)
    result = models.ForeignKey(Result, on_delete=models.PROTECT, verbose_name="Result Id", blank=False, null=False)

    def __str__(self):
        return '{} - {}'.format(self.id, self.time)

    class Meta:
        verbose_name_plural = "Fastest Laps"



