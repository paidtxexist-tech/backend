from rest_framework import serializers
from homepage.models import Plan
from payment.models import Subscription, Payment
from django.contrib.auth.models import User

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    vpn_key = serializers.CharField(source='vpn_key.key', read_only=True, default=None)
    class Meta:
        model = Subscription
        fields = ['id', 'plan', 'start_date', 'end_date', 'is_active', 'vpn_key']

class PaymentSerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(source='plan.name', read_only=True)
    class Meta:
        model = Payment
        fields = ['id', 'money', 'datetime', 'plan_name']