from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import FaqSerializer
from .models import Faq
from rest_framework.views import APIView
from rest_framework.response import Response


# get faq lists or add new faq
class FaqListAPIView(APIView):
    def get(self, request):
        serializer = FaqSerializer(
            Faq.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get faq detail or update/delete faq
class FaqDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Faq, pk=pk)

    def get(self, request, pk, format=None):
        faq = self.get_object(pk)
        serializer = FaqSerializer(faq)
        return Response(serializer.data)

    def put(self, request, pk):
        faq = self.get_object(pk)
        serializer = FaqSerializer(faq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        faq = self.get_object(pk)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
