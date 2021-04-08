from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Country'

    def __str__(self):
        return f'{self.name}'
