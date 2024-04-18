from django.db import models
from analytics.models.drivers import Driver
from analytics.models.races import Race


class PitStop(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Pit Stop ID", blank=False, null=False)
    stop = models.IntegerField(verbose_name='Stop', blank=False, null=False)
    lap = models.IntegerField(verbose_name='Lap', blank=False, null=False)
    miles = models.IntegerField(verbose_name='Time in Miles', blank=False, null=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Gran Prix", blank=False, null=False)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, verbose_name="Driver", blank=False, null=False)


    def __str__(self):
        return '{} - {} - {}'.format(self.lap, self.driver, self.race)


    class Meta:
        verbose_name_plural = "Pit Stops"

