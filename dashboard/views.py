from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from payment.models import Subscription, Payment
from django.db import connection

@login_required
def dashboard(request):
    """панель управления подписками"""
    user = request.user
    active_subscriptions = Subscription.objects.filter(user=user, is_active=True)
    payments = Payment.objects.filter(user=user).order_by('-datetime')


    context = {
        'active_subscriptions': active_subscriptions,
        'payments': payments,
    #    'total_spent': total_spent
    }
    return render(request, 'dashboard.html', context)