from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout


class RegisterView(CreateView):
    """регистрация"""
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage')

def logout_view(request):
    """выход"""
    logout(request)
    return redirect('homepage')