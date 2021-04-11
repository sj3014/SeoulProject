from rest_framework import serializers
from .models import Student
from apps.quarantine.serializers import QuarantineSerializer
from apps.address.serializers import AddressSerializer


class StudentSerializer(serializers.ModelSerializer):
    quarantine = QuarantineSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
