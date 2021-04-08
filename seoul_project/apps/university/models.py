from django.db import models
import uuid
from django.utils import timezone


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    area = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    # uniqueID???

    class Meta:
        db_table = 'University'

    def __str__(self):
        return f'{self.name}'
