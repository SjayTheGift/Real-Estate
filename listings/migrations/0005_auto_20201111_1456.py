# Generated by Django 3.1.3 on 2020-11-11 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201111_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]