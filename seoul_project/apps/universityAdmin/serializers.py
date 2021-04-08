from rest_framework import serializers
from .models import UniversityAdmin


class UniversityAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityAdmin
        fields = '__all__'
