from django.db import models


class Circuit(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Circuit ID", blank=False, null=False)
    ref = models.CharField(max_length=100, verbose_name='Circuit Ref', blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name="Circuit Name", blank=False, null=False)
    city = models.CharField(max_length=100, verbose_name="City", blank=False, null=False)
    country_flag = models.ImageField(upload_to="analytics/flags/%Y/%m/%d/", blank=True, default='')
    country = models.CharField(max_length=100, verbose_name="Country", blank=False, null=False)
    latitude = models.FloatField(verbose_name="Latitude", blank=False, null=False)
    longitude = models.FloatField(verbose_name="Longitude", blank=False, null=False)
    altitude = models.IntegerField(verbose_name="Altitude", blank=True, null=False)
    url = models.CharField(max_length=100, verbose_name="Circuit Wiki Url", blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Circuits"



