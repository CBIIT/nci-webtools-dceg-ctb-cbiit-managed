# Generated by Django 3.2.13 on 2022-10-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0002_auto_20221010_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='diagnosis',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
