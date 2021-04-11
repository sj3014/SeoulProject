from django.db import models
from django.utils import timezone


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Announcement'

    def __str__(self):
        return f'{self.title}'
