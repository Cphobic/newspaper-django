from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_photos')
