from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    description = models.CharField(max_length=100, verbose_name='Description', null=False)
    is_deleted = models.BooleanField(verbose_name="Is Deleted?", null=False, blank=False, default=False)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['-id']

    def __str__(self):
        return "{}".format(self.description)

