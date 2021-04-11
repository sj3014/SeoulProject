from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import AnnouncementSerializer
from .models import Announcement
from rest_framework.views import APIView
from rest_framework.response import Response


# get announcement lists or add new announcement
class AnnouncementListAPIView(APIView):
    def get(self, request):
        serializer = AnnouncementSerializer(
            Announcement.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get announcement detail or update/delete announcement
class AnnouncementDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Announcement, pk=pk)

    def get(self, request, pk, format=None):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

    def put(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(
            announcement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        announcement = self.get_object(pk)
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
