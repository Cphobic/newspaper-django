from django.db import models
from django.utils import timezone
from django.urls import reverse

from accounts.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title[:30]}...'

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
