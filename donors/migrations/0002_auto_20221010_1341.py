# Generated by Django 3.2.13 on 2022-10-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='diagnosis',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]