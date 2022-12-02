# Generated by Django 3.2.13 on 2022-10-13 08:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0010_auto_20221013_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinical_treatment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 8, 8, 31, 665231, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clinical_treatment',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 8, 8, 31, 665255, tzinfo=utc)),
        ),
    ]
