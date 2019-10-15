from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics',
                              verbose_name='Avatar')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])
