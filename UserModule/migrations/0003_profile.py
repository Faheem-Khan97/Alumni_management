# Generated by Django 3.0.6 on 2020-06-05 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserModule', '0002_auto_20200603_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passout_year', models.IntegerField(blank=True, null=True)),
                ('home_city', models.CharField(blank=True, max_length=120, null=True)),
                ('current_city', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('working', models.CharField(blank=True, max_length=120, null=True)),
                ('work_history', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
