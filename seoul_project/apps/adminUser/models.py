from django.db import models
import uuid


class AdminUser(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    phoneNumber = models.CharField(max_length=12, blank=True, null=True)
    isVerified = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    # uniqueID???

    class Meta:
        db_table = 'AdminUser'

    def __str__(self):
        return f'{self.email}'