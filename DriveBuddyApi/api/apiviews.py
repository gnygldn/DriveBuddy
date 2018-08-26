from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Trip, Driver
from .serializers import DriverSerializer, TripSerializer
from django.contrib.auth import authenticate
import datetime
import sys
import status

class LoginView(APIView):
	permission_classes = ()
	def post(self, request,):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username, password=password)
		if user:
			return Response({"token": user.auth_token.key})
		else:
			return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class list_of_trips(generics.ListCreateAPIView):
	queryset = Trip.objects.all()
	serializer_class = TripSerializer

class list_of_drivers(generics.ListCreateAPIView):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer

class driver_details(generics.RetrieveDestroyAPIView):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer

class driver_create(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes = ()
	serializer_class = DriverSerializer

class list_of_trips_selected_between_dates(APIView):
	def get(self, request, date1):
		date = str(date1)
		startyear = int(date[:4])
		startmonth = int(date[4:6])
		startday = int(date[6:8])
		endyear = int(date[8:12])
		endmonth = int(date[12:14])
		endday = int(date[14:])
		start = datetime.date(startyear,startmonth,startday)
		end = datetime.date(endyear,endmonth,endday)
		trips = Trip.objects.all()
		filteredtrips = []
		for trip in trips:
			tripend = trip.start_date + datetime.timedelta(days = trip.duration)
			if trip.start_date.date() <= start and tripend.date() >= end:
				print(trip)
				filteredtrips.append(trip)
		data = TripSerializer(filteredtrips, many=True).data
		return Response(data)

