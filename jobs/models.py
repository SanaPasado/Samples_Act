from django.urls import reverse

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Job(models.Model):
    job_title = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_description = models.TextField
    min_offer = models.CharField
    max_offer = models.CharField
    location = models.CharField


    def __str__(self):
        return self.content

    # def get_absolute_url(self):
    #     return reverse("tweets:detail_view", kwargs={"pk": self.pk})
