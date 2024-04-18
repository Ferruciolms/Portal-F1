from django.db import models

class Season(models.Model):
    year = models.IntegerField(verbose_name="year", blank=False, null=False)
    url = models.CharField(max_length=250, verbose_name="Season Url", blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.year)


    class Meta:
        verbose_name_plural = "Seasons"
