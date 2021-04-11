from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import AddressSerializer
from .models import Address
from rest_framework.views import APIView
from rest_framework.response import Response


# get address lists or add new address
class AddressListAPIView(APIView):
    def get(self, request):
        serializer = AddressSerializer(Address.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get address detail or update/delete address
class AddressDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Address, pk=pk)

    def get(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, pk):
        address = self.get_object(pk)
        serializer = AddressSerializer(
            address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
