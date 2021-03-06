# Generated by Django 3.2.5 on 2021-07-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('qual', models.CharField(choices=[('имп', 'ИМП'), ('ч', 'Ч'), ('чда', 'ЧДА'), ('хч', 'ХЧ'), ('осч', 'ОСЧ'), ('----------', '----------')], default='----------', max_length=10, verbose_name='Квалификация')),
                ('clas', models.CharField(default='не опасен', max_length=15, verbose_name='Класс опасности')),
                ('date', models.DateField(verbose_name='Дата изготовления')),
                ('prov', models.CharField(blank=True, max_length=20, null=True, verbose_name='Поставщик')),
                ('srok', models.DateField(blank=True, null=True, verbose_name='Срок годности')),
                ('place', models.CharField(max_length=30, verbose_name='Место хранения')),
                ('mass', models.FloatField(blank=True, null=True, verbose_name='Масса, кг')),
            ],
        ),
    ]
