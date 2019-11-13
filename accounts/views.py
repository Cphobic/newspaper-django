from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


from paper.models import Post


from . import forms
from .models import CustomUser


class SignupView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'


class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = 'accounts/login.html'
    success_message = 'You are logged in'


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/update_account.html'
    form_class = forms.CustomUserChangeForm
    model = CustomUser
    # fields = ['username', 'email', 'image']
    success_url = reverse_lazy('home')


class AllPostList(LoginRequiredMixin, generic.ListView):
    template_name = 'accounts/all_posts.html'
    model = Post
    ordering = ['-pub_date']
    paginate_by = 2
    context_object_name = 'posts'

    def get_queryset(self):
        self.user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        return Post.objects.filter(author=self.user)
