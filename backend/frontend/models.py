from django.db import models
from django.contrib.auth.models import User


class ApiKeys(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    api_ukraine = models.CharField(max_length=200, blank=True)
    api_bodis = models.CharField(max_length=200, blank=True)


class Some:
    pass