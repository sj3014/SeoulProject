from rest_framework import serializers
from .models import Quarantine


class QuarantineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarantine
        fields = '__all__'
