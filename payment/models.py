from django.db import models
from django.contrib.auth.models import User
from homepage.models import Plan

class Payment(models.Model):
    """пока нет платёжного шлюза, просто имитирует оплату"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=7, decimal_places=2)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.money} руб. {self.datetime.strftime('%H:%M %d.%m.%Y')}"


class Subscription(models.Model):
    """подписка
    p.s. возможно, стоит вынести в отдельное приложение, но для mvp пусть будет здесь, а в дашборде юзера импорт"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.user} до {self.end_date.strftime('%d.%m.%Y')}"
