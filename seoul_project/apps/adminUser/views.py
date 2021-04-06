from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import AdminUserSerializer
from .models import AdminUser
from rest_framework.views import APIView
from rest_framework.response import Response


# get admin lists or add new admin
class AdminUserListAPIView(APIView):
    def get(self, request):
        serializer = AdminUserSerializer(AdminUser.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get adminUser detail or update/delete adminUser
class AdminUserDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(AdminUser, pk=pk)

    def get(self, request, pk, format=None):
        adminUser = self.get_object(pk)
        serializer = AdminUserSerializer(pk)
        return Response(serializer.data)

    def put(self, request, pk):
        adminUser = self.get_object(pk)
        serializer = AdminUserSerializer(adminUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        adminUser = self.get_object(pk)
        adminUser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
