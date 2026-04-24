from django.shortcuts import render
from .models import Plan

def index(request):
    """главная страница"""
    plans = Plan.objects.all()
    return render(request, 'index.html', {'plans': plans})
