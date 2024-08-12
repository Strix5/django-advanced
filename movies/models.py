from django.db import models


class Movie(models.Model):
    class Status(models.TextChoices):
        WATCHED = 'WA', 'Watched'
        UNWATCHED = 'UN', 'Unwatched'

    name = models.CharField(max_length=100)
    description = models.TextField()
    length = models.SmallIntegerField(verbose_name='Длительность', help_text='Длительность в минутах')
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.UNWATCHED)

    def __str__(self):
        return self.name
