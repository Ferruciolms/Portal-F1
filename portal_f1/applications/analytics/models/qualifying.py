from django.db import models
from analytics.models.constructors import Constructor
from analytics.models.drivers import Driver
from analytics.models.races import Race


class Qualifying(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Qualifying ID", blank=False, null=False)
    number = models.IntegerField(verbose_name="Number driver", null=False, blank=False)
    position = models.IntegerField(verbose_name='Position', blank=False, null=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Gran Prix", blank=False, null=False)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, verbose_name="Driver", blank=False, null=False)
    constructor = models.ForeignKey(Constructor, on_delete=models.PROTECT, verbose_name="Construtor", blank=False, null=False)


    def __str__(self):
        return '{}'.format(self.race)

    class Meta:
        verbose_name_plural = "Qualifyings"
