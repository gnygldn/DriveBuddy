from rest_framework import serializers
from .models import Trip, Driver, Manager
from rest_framework.authtoken.models import Token

class TripSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trip
		fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = ('name', 'email_address','score' , 'password')
		extra_kwargs = {'password': {'write_only': True}}
		#fields = '__all__'
	def create(self, validated_data):
		driver = Driver(email_address=validated_data['email_address'], name=validated_data['name'], score=validated_data['score'] )
		driver.set_password(validated_data['password'])
		driver.save()
		Token.objects.create(user=driver)
		return driver


class ManagerSerialier(serializers.ModelSerializer):
	class Meta:
		model = Manager
		fields = '__all__'



