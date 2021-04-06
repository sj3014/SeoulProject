from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ("uuid", 'email', 'password', 'firstName', 'lastName', 'phoneNumber', 'kakaoID',
        #           'currentLocation', 'isVerified', 'arrivalDateTime')
        fields = '__all__'
