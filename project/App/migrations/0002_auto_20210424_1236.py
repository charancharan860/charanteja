# Generated by Django 3.0 on 2021-04-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handicrafts',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]