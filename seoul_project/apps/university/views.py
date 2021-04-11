from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import UniversitySerializer
from .models import University
from rest_framework.views import APIView
from rest_framework.response import Response


# get university lists or add new university
class UniversityListAPIView(APIView):
    def get(self, request):
        serializer = UniversitySerializer(University.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get university detail or update/delete university
class UniversityDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(University, pk=pk)

    def get(self, request, pk, format=None):
        university = self.get_object(pk)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)

    def put(self, request, pk):
        university = self.get_object(pk)
        serializer = UniversitySerializer(
            university, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        university = self.get_object(pk)
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
