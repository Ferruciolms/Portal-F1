from django.db import models
from analytics.models.sprint_results import SprintResult


class SprintFastestLap(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Sprint Fastest Lap ID", blank=False, null=False)
    lap = models.IntegerField(verbose_name="Sprint Lap", blank=False, null=False)
    time = models.TimeField(verbose_name="Sprint fastest lap time", blank=False, null=False)
    sprint_result = models.ForeignKey(SprintResult, on_delete=models.PROTECT, verbose_name="Sprint Result Id", blank=False, null=False)

    def __str__(self):
        return '{} - {}'.format(self.id, self.time)

    class Meta:
        verbose_name_plural = "Sprint Fastest Laps"