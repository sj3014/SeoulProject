from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import QuarantineSerializer
from .models import Quarantine
from rest_framework.views import APIView
from rest_framework.response import Response


# get quarantine lists or add new quarantine
class QuarantineListAPIView(APIView):
    def get(self, request):
        serializer = QuarantineSerializer(Quarantine.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuarantineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get quarantine detail or update/delete quarantine
class QuarantineDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Quarantine, pk=pk)

    def get(self, request, pk, format=None):
        quarantine = self.get_object(pk)
        serializer = QuarantineSerializer(pk)
        return Response(serializer.data)

    def put(self, request, pk):
        quarantine = self.get_object(pk)
        serializer = QuarantineSerializer(quarantine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quarantine = self.get_object(pk)
        quarantine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
