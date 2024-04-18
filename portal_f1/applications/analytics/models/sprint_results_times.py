from django.db import models
from analytics.models.sprint_results import SprintResult


class SprintResultTime(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Time in milliseconds ID", blank=False, null=False)
    milliseconds = models.IntegerField(verbose_name="Time in Milliseconds", blank=True, null=True)
    sprint_result = models.ForeignKey(SprintResult, on_delete=models.PROTECT, verbose_name="Sprint Result ID", blank=False, null=False)

    def __str__(self):
        return "{}".format(self.milliseconds)

    class Meta:
        verbose_name_plural = "Milliseconds"
