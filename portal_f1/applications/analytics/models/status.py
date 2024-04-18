from django.db import models

class Status(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="status_id", blank=False, null=False)
    name = models.CharField(max_length=65, verbose_name="status name", blank=False, null=False)

    def __str__(self):
        return "{}".format(self.name)


    class Meta:
        verbose_name_plural = "status"
