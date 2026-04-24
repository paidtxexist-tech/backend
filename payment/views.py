from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from homepage.models import Plan
from django.utils import timezone
from datetime import timedelta
from payment.models import Subscription, Payment


@login_required
def checkout(request, plan_id):
    """оплата"""
    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == "GET":
        # открывается страница оплаты
        return render(request, 'checkout.html', {'plan': plan})
    elif request.method == "POST":
        # принимаются данные от пользователя
        now = timezone.now()
        duration = timedelta(days=plan.duration)
        end_date = now + duration
        sub = Subscription.objects.create(user=request.user, plan=plan, start_date=now, end_date=end_date, is_active=True)
        pay = Payment.objects.create(user=request.user, plan=plan, money=plan.price)
        return redirect('payment_success')

@login_required
def payment_success(request):
    """успешная оплата"""
    return render(request, 'success.html')

