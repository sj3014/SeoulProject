from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import UniversityAdminSerializer
from .models import UniversityAdmin
from rest_framework.views import APIView
from rest_framework.response import Response


# get admin lists or add new admin
class UniversityAdminListAPIView(APIView):
    def get(self, request):
        serializer = UniversityAdminSerializer(
            UniversityAdmin.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniversityAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get universityAdmin detail or update/delete universityAdmin
class UniversityAdminDetailAPIView(APIView):
    def get_object(self, uuid):
        return get_object_or_404(UniversityAdmin, uuid=uuid)

    def get(self, request, uuid, format=None):
        universityAdmin = self.get_object(uuid)
        serializer = UniversityAdminSerializer(uuid)
        return Response(serializer.data)

    def put(self, request, uuid):
        universityAdmin = self.get_object(uuid)
        serializer = UniversityAdminSerializer(
            universityAdmin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        universityAdmin = self.get_object(uuid)
        universityAdmin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
