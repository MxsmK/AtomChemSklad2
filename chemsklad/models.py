from django.db import models


class React(models.Model):
    qual_list = (('имп', 'ИМП'), ('ч', 'Ч'), ('чда', 'ЧДА'), ('хч', 'ХЧ'), ('осч', 'ОСЧ'), ('----------', '----------'))
    name = models.CharField(verbose_name="Название", max_length=30)
    qual = models.CharField(verbose_name="Квалификация", max_length=10, choices=qual_list, default='----------')
    clas = models.CharField(verbose_name='Класс опасности', max_length=15, default='не опасен')
    date = models.DateField(verbose_name="Дата изготовления")
    prov = models.CharField(verbose_name="Поставщик", max_length=20, null=True, blank=True)
    srok = models.DateField(verbose_name="Срок годности", null=True, blank=True)
    place = models.CharField(verbose_name="Место хранения", max_length=30)
    mass = models.FloatField(verbose_name="Масса, кг", null=True, blank=True)

    def add(self):
        self.save()

    def __str__(self):
        return str(self.name)
