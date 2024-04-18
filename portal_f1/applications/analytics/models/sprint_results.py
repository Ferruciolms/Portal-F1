from django.db import models
from analytics.models.constructors import Constructor
from analytics.models.drivers import Driver
from analytics.models.races import Race
from analytics.models.status import Status


class SprintResult(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Sprint Result ID", blank=False, null=False)
    number = models.IntegerField(verbose_name="Number driver", null=False, blank=False)
    grid = models.IntegerField(verbose_name="Sprint Starting Grid Position", blank=False, null=False)
    position = models.IntegerField(verbose_name="Sprint Final Position", blank=False, null=True)
    position_text = models.CharField(max_length=65, verbose_name="Sprint Position txt", blank=False, null=False)
    position_order = models.IntegerField(verbose_name="Sprint Position order", blank=False, null=False)
    points = models.FloatField(verbose_name="Sprint Points", blank=False, null=True)
    laps = models.IntegerField(verbose_name="Sprint Laps", blank=False, null=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Sprint Race ID", blank=False, null=False)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, verbose_name="Driver ID", blank=False, null=False)
    constructor = models.ForeignKey(Constructor, on_delete=models.PROTECT, verbose_name="Constructor ID", blank=False, null=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Sprint Status", blank=False, null=False)


    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.driver, self.race)

    class Meta:
        verbose_name_plural = "Sprint results"
