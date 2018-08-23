from rest_framework import serializers
from .models import Trip, Driver, Manager

class TripSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trip
		fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = '__all__'

class ManagerSerialier(serializers.ModelSerializer):
	class Meta:
		model = Manager
		fields = '__all__'



