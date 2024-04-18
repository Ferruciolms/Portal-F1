from django.db import models
from django.conf import settings
from datetime import datetime

CREATE = 1
UPDATE = 2
DELETE = 3

class Log(models.Model):


    Type_choices = [
        (CREATE, 'Create'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete')
    ]

    id = models.AutoField(primary_key=True, verbose_name='ID')
    date = models.DateTimeField(verbose_name='Date', null=False)
    type = models.IntegerField(choices=Type_choices, verbose_name='Type', null=False)
    model = models.CharField(max_length=100, verbose_name='Model', null=False)
    data = models.TextField(verbose_name='Data', null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='User', null=False, blank=False)
    model_id = models.BigIntegerField(verbose_name='Model ID', null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Logs'
        ordering = ['-id']

    def __str__(self):
        return "date: {} - type: {} - model: {} - data: {} - user: {}".format(self.date, self.type, self.model, self.data, self.user)
    
