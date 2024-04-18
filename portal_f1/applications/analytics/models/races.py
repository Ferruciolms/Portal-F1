from django.db import models
from analytics.models.circuits import Circuit



class Race(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Race ID", null=False, blank=False)
    year = models.IntegerField(verbose_name="Year", blank=False, null=False)
    round = models.IntegerField(verbose_name="Round", blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name= "GP Name", blank=False, null=False)
    date = models.DateField(verbose_name="Date", blank=False, null=False)
    time = models.TimeField(verbose_name="Time", blank=False, null=True)
    url = models.CharField(max_length=250, verbose_name="Race Url", blank=False, null=False)
    circuit = models.ForeignKey(Circuit, on_delete=models.PROTECT, verbose_name="Circuit ID", blank=False, null=False)

    def __str__(self):
        return '{} - {}'.format(self.year, self.name)


    class Meta:
        verbose_name_plural = "Races"


