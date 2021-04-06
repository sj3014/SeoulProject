from django.db import models
import uuid


class University(models.Model):
    name = models.EmailField(unique=True)
    address = models.TextField()
    area = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    # uniqueID???

    class Meta:
        db_table = 'University'

    def __str__(self):
        return f'{self.name}'
