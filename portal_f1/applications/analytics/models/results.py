from django.db import models
from analytics.models.constructors import Constructor
from analytics.models.drivers import Driver
from analytics.models.races import Race
from analytics.models.status import Status


class Result(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Result ID", blank=False, null=False)
    number = models.IntegerField(verbose_name="Number driver", null=True, blank=True)
    grid = models.IntegerField(verbose_name="Starting Grid Position", blank=False, null=False)
    position = models.IntegerField(verbose_name="Final Position", blank=False, null=True)
    position_text = models.CharField(max_length=65, verbose_name="Position txt", blank=False, null=False)
    position_order = models.IntegerField(verbose_name="Position order", blank=True, null=True)
    points = models.FloatField(verbose_name="Points", blank=False, null=False)
    laps = models.IntegerField(verbose_name="Laps", blank=False, null=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Race ID", blank=False, null=False)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, verbose_name="Driver ID", blank=False, null=False)
    constructor = models.ForeignKey(Constructor, on_delete=models.PROTECT, verbose_name="Constructor ID", blank=False, null=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Status", blank=False, null=False)


    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name_plural = "Results"
