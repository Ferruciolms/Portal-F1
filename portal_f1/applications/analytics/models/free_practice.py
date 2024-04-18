from django.db import models
from analytics.models.races import Race


class FreePractice(models.Model):
    TYPE = [
       (1, "FP1"),
       (2, "FP2"),
       (3, "FP3")
    ]

    id = models.BigAutoField(primary_key=True, verbose_name="Free Practice ID", blank=False, null=False)
    type = models.IntegerField(verbose_name="Type session", choices=TYPE, null=False, blank=False)
    date = models.DateField(verbose_name="Free Practice Date", null=False, blank=False)
    time = models.TimeField(verbose_name="Free Practice Time", null=False, blank=True)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, null= False, blank=False)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = "Free Practices"

