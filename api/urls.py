from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plan_list, name='api_plans'),
    path('subscriptions/', views.my_subscriptions, name='api_subscriptions'),
    path('payment/', views.create_payment, name='api_payment'),
    path('payments/', views.payment_history, name='api_payments'),
]