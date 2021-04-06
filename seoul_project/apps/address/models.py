from django.db import models


class Address(models.Model):
    address = models.TextField()
    enAddress = models.TextField()
    addressDetail = models.TextField()
    zipCode = models.IntegerField()
    lat = models.FloatField()
    lang = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Address'
