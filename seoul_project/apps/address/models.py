from django.db import models
from django.utils import timezone


class Address(models.Model):
    address = models.TextField()
    english_address = models.TextField()
    address_detail = models.TextField()
    zipcode = models.IntegerField()
    lat = models.FloatField()
    lang = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Address'

    def __str__(self):
        return f'{self.address}'
