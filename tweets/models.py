from django.urls import reverse

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("tweets:detail_view", kwargs={"pk": self.pk})
