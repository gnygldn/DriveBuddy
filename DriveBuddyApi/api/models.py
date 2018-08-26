from django.db import models

# Create your models here.

class Trip(models.Model):
	distance = models.IntegerField()
	start_date = models.DateTimeField()
	duration = models.IntegerField()

	def __str__(self):
		return '{} {} {}'.format(self.distance, self.start_date, self.duration)

class Driver(models.Model):
	name = models.CharField(max_length = 30)	
	email_address = models.CharField(max_length = 40,default='')
	score = models.IntegerField()
	password = models.CharField(max_length = 30,default='password')

	def __str__(self):
		return '{} {} {}'.format(self.name, self.email_address, self.score)

	def set_password(self, password):
		self.password = password

class Manager(models.Model):
	name = models.CharField(max_length = 30)
	email_address = models.CharField(max_length = 40)

	def __str__(self):
		return '{} {}'.format(self.name, self.email_address)