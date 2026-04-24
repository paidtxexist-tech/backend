from django.db import models

class Plan(models.Model):
    """тарифные планы на главной странце"""
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    duration = models.IntegerField(verbose_name='Длительность') # в днях
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена') # в рублях, напр. 12 345,99

    class Meta:
        verbose_name = 'Тариф'

    def __str__(self):
        return f'{self.name} - {self.price} руб.'
