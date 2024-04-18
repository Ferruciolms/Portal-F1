from django.db import models


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Driver ID", blank=False, null=False)
    Ref = models.CharField(max_length=65, null=True, blank=True)
    number = models.IntegerField(verbose_name="Number driver", null=False, blank=False)
    code = models.CharField(max_length=3, verbose_name="Code Driver", null=False, blank=False)
    fname = models.CharField(max_length=65, verbose_name="First Name", null=False, blank=False)
    lname = models.CharField(max_length=65, verbose_name="Last Name", null=False, blank=False)
    dob = models.DateField(verbose_name="Date of Birthday", null=False, blank=False)
    nationality = models.CharField(max_length=65, verbose_name="Nationality", null=False, blank=False)
    url = models.CharField(max_length=250, verbose_name="Url Driver", null=False, blank=False)

    def __str__(self):
        return "{}".format(self.Ref)

    class Meta:
        verbose_name_plural = "Drivers"

