from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Trip, Driver
from .serializers import DriverSerializer, TripSerializer

class list_of_trips(generics.ListCreateAPIView):
	queryset = Trip.objects.all()
	serializer_class = TripSerializer

class list_of_drivers(generics.ListCreateAPIView):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer

class driver_details(generics.RetrieveDestroyAPIView):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer

