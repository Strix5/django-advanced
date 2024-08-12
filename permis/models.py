from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Catalog(models.Model):
    STATUS_CHOICES = (
        (True, 'True'),
        (False, 'False'),
    )

    title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(max_length=5, choices=STATUS_CHOICES, default=False)

    def __str__(self):
        return self.title
