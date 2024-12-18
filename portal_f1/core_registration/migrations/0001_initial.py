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
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=45, verbose_name='Description')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted?')),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted?')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('acronym', models.CharField(max_length=2, verbose_name='Sigla')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted?')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_registration.country', verbose_name='País')),
            ],
            options={
                'verbose_name_plural': 'States',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration date')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted?')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_registration.city', verbose_name='City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User who registered the company ')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_registration.state'),
        ),
    ]
