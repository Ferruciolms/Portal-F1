from django.db import models


class Constructor(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Constructor ID", blank=False, null=False)
    ref = models.CharField(max_length=100, verbose_name="REF name", blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name="Name", blank=False, null=False)
    nationality = models.CharField(max_length=100, verbose_name="Nationality", blank=False, null=False)
    url = models.CharField(max_length=250, verbose_name="Constructor Wiki Url", blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.ref)

    class Meta:
        verbose_name_plural = "Constructors"

