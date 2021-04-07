from django.db import models
import uuid


class Quarantine(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    firstTest = models.CharField(max_length=20, default='untested')
    secondTest = models.CharField(max_length=20, default='untested')
    status = models.CharField(max_length=20, default='outOfKorea')

    class Meta:
        db_table = 'Quarantine'

    def __str__(self):
        return f'{self.uuid}'
