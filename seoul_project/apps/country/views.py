from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import CountrySerializer
from .models import Country
from rest_framework.views import APIView
from rest_framework.response import Response


# get country lists or add new country
class CountryListAPIView(APIView):
    def get(self, request):
        serializer = CountrySerializer(Country.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get country detail or update/delete country
class CountryDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Country, pk=pk)

    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(pk)
        return Response(serializer.data)

    def put(self, request, pk):
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        country = self.get_object(pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
