from django.db import models
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField()
    created = models.DateField(default=timezone.now())
    played = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.created})'
