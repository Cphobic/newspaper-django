from django.shortcuts import render
from .forms import UserCreationForm
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


# def HomeView(request):
#     form = UserCreationForm(request.POST)
#     return render(request, 'home.html', {'form': form})

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'home.html'
