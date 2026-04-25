from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from .serializers import PlanSerializer, SubscriptionSerializer, PaymentSerializer
from homepage.models import Plan
from payment.models import Subscription, Payment, VPNKey

@api_view(['GET'])
@permission_classes([AllowAny])
def plan_list(request):
    """список всех активных тарифов"""
    plans = Plan.objects.all()
    serializer = PlanSerializer(plans, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):
    """
    создаёт платёж
    """
    plan_id = request.data.get('plan_id')
    if not plan_id:
        return Response({'error': 'План не выбран'}, status=400)

    try:
        plan = Plan.objects.get(pk=plan_id)
    except Plan.DoesNotExist:
        return Response({'error': 'План не найден'}, status=404)

    vpn_key = VPNKey.objects.filter(is_used=False).first()
    if not vpn_key:
        return Response({'error': 'Нет доступных VPN-ключей'}, status=503)

    """господи, как же я ненавижу сериализаторы..."""

    end_date = timezone.now() + timedelta(days=plan.duration)
    sub = Subscription.objects.create(
        user=request.user,
        plan=plan,
        start_date=timezone.now(),
        end_date=end_date,
        is_active=True
    )

    pay = Payment.objects.create(
        user=request.user,
        plan=plan,
        money=plan.price,
    )
    # когда будет платёжный шлюз, здесь нужно будет проверять статус оплаты перед тем, как выдавать ключ
    vpn_key.subscription = sub
    vpn_key.is_used = True
    vpn_key.save()

    serializer = SubscriptionSerializer(sub)
    return Response(serializer.data, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_subscriptions(request):
    """текущие подписки у пользователя"""
    subs = Subscription.objects.filter(user=request.user, is_active=True)
    serializer = SubscriptionSerializer(subs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_history(request):
    """история платежей"""
    payments = Payment.objects.filter(user=request.user).order_by('-datetime')
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)

