from django.db import models
from analytics.models.results import Result


class ResultTime(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Time in milliseconds ID", blank=False, null=False)
    milliseconds = models.IntegerField(verbose_name="Time in Milliseconds", blank=True, null=True)
    result = models.ForeignKey(Result, on_delete=models.PROTECT, verbose_name="Result ID", blank=False, null=False)

    def __str__(self):
        return "{}".format(self.milliseconds)

    class Meta:
        verbose_name_plural = "Milliseconds"
