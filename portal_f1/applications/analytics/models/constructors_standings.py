from django.db import models
from analytics.models.constructors import Constructor
from analytics.models.races import Race


class ConstructorStanding(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Constructor Standing ID", blank=False, null=False)
    points = models.FloatField(verbose_name="Points", blank=False, null=False)
    position = models.IntegerField(verbose_name='Position', blank=False, null=False)
    position_text = models.CharField(verbose_name='Position Txt', max_length=65, blank=False, null=False)
    wins = models.IntegerField(verbose_name="Wins", blank=False, null=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Gran Prix", blank=False, null=False)
    constructor = models.ForeignKey(Constructor, on_delete=models.PROTECT, verbose_name="Constructor", blank=False, null=False)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.constructor, self.race)

    class Meta:
        verbose_name_plural = "Constructors Standings"
