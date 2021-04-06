from django.db import models
import uuid


class User(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    phoneNumber = models.CharField(max_length=12, blank=True, null=True)
    kakaoID = models.CharField(max_length=50, blank=True, null=True)
    currentLocation = models.TextField(blank=True, null=True)
    isVerified = models.BooleanField(default=False)
    arrivalDateTime = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return f'{self.email}'
