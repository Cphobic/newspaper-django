from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as home_views


urlpatterns = [
    path('', home_views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>/', home_views.DetailPostView.as_view(), name='detail'),
    path('update/<int:pk>/', home_views.EditPostView.as_view(), name='update_post'),
    path('create/', home_views.CreatePostView.as_view(), name='create_post'),
    path('delete/<int:pk>/', home_views.DeletePostView.as_view(), name='delete_post'),
]
