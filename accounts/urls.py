from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views as account_views


urlpatterns = [
    path('signup/', account_views.SignupView.as_view(), name='signup'),

    path('login/', account_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password-change-form/',
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/password_change_form.html',
             success_url=reverse_lazy('login')), name='password-change'),

    path('update-profile/<int:pk>/', account_views.UpdateProfileView.as_view(),
         name='update_profile'),
]
