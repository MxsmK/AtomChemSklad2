# Generated by Django 3.2.5 on 2021-07-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemsklad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='react',
            name='mass_True',
            field=models.FloatField(blank=True, null=True, verbose_name='Масса, кг'),
        ),
        migrations.AlterField(
            model_name='react',
            name='mass',
            field=models.FloatField(blank=True, null=True, verbose_name='Изначальная масса, кг'),
        ),
    ]
