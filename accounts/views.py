from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin

from . import forms
from .models import CustomUser


class SignupView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'


class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = 'accounts/login.html'
    success_message = 'You are logged in'


class UpdateProfileView(generic.UpdateView):
    template_name = 'accounts/update_account.html'
    form_class = forms.CustomUserChangeForm
    model = CustomUser
    # fields = ['username', 'email', 'image']
    success_url = reverse_lazy('home')
