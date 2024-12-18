# Generated by Django 4.0.5 on 2024-09-30 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('type', models.IntegerField(choices=[(1, 'Create'), (2, 'Update'), (3, 'Delete')], verbose_name='Type')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('data', models.TextField(verbose_name='Data')),
                ('model_id', models.BigIntegerField(verbose_name='Model ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Logs',
                'ordering': ['-id'],
            },
        ),
    ]
