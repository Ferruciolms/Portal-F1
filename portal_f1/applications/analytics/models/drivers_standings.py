from django.db import models
from analytics.models.drivers import Driver
from analytics.models.races import Race


class DriverStanding(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Driver Standing ID", blank=False, null=False)
    points = models.FloatField(verbose_name="Points", blank=False, null=False)
    position = models.IntegerField(verbose_name='Position', blank=False, null=False)
    position_text = models.CharField(verbose_name='Position Txt', max_length=65, blank=False, null=False)
    wins = models.IntegerField(verbose_name="Wins", blank=False, null=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Gran Prix", blank=False, null=False)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, verbose_name="Driver", blank=False, null=False)


    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.driver, self.race)

    class Meta:
        verbose_name_plural = "Drivers Standings"
