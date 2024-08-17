from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Game(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'))
    price = models.CharField(verbose_name=_('Price'))
    created = models.DateField(default=timezone.now())
    played = models.BooleanField(verbose_name=_('Played'), default=False)

    def __str__(self):
        return f'{self.name} ({self.created})'
