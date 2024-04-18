from django.db import models
from analytics.models.constructors import Constructor
from analytics.models.races import Race


class ConstructorResult(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Constructor Result ID", blank=False, null=False)
    points = models.FloatField(verbose_name="Points", blank=False, null=False)
    status = models.CharField(max_length=65, verbose_name="status", blank=False, null=False)
    constructor = models.ForeignKey(Constructor, on_delete=models.PROTECT, verbose_name="Construtor", blank=False, null=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Gran Prix", blank=False, null=False)


    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.constructor, self.race)

    class Meta:
        verbose_name_plural = "Constructors Results"
