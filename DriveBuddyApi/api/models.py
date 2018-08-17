from django.db import models

# Create your models here.

class Trip(models.Model):
	distance = models.IntegerField()
	start_date = models.DateTimeField(auto_now=True)
	duration = models.IntegerField()

	def __str__(self):
		return (self.distance,self.start_date,self.duration)

class Driver(models.Model):
	name = models.CharField(max_length = 30)
	emailAddress = models.CharField(max_length = 40)
	score = models.IntegerField()

	def __str__(self):
		return (self.name)

class Manager(models.Model):
	name = models.CharField(max_length = 30)
	emailAddress = models.CharField(max_length = 40)

	def __str__(self):
		return (self.name)