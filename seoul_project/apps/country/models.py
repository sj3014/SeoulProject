from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    countryCode = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Country'

    def __str__(self):
        return f'{self.name}'
