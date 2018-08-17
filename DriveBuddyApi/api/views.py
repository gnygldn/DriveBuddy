from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Trip, Driver
# Create your views here.

def list_of_trips(request):
	trips = Trip.objects.all()
	data = {"trips": list(trips.values("distance", "start_date", "duration"))}
	return JsonResponse(data)

def list_of_drivers(request):
	drivers = Driver.objects.all()
	data = {"drivers": list(drivers.values("name","email_address","score"))}
	return JsonResponse(data)