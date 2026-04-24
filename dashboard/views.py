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

    # with connection.cursor() as cursor:
    #     cursor.execute("""
    #     SELECT SUM(money) FROM payment_payment
    #     WHERE user_id = %s AND is_success = 1
    #     """, [user.id])
    #     total_spent = cursor.fetchone()[0] or 0

    context = {
        'active_subscriptions': active_subscriptions,
        'payments': payments,
    #    'total_spent': total_spent
    }
    return render(request, 'dashboard.html', context)