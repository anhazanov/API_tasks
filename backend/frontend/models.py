from django.db import models
from django.conf import settings


class ApiKeys(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    api_ukraine = models.CharField(max_length=200, blank=True)
    api_bodis = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'API ключ'
        verbose_name_plural = 'API ключи'

    def __str__(self):
        return f"{self.username} | api_ukraine - {self.api_ukraine} | api_bodis - {self.api_bodis}"

