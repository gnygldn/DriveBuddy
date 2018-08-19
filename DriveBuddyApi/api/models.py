from django.db import models

# Create your models here.

class Trip(models.Model):
	distance = models.IntegerField()
	start_date = models.DateTimeField(auto_now=True)
	duration = models.IntegerField()

	def __str__(self):
		return '{} {} {}'.format(self.distance, self.start_date, self.duration)

class Driver(models.Model):
	name = models.CharField(max_length = 30)
	email_address = models.CharField(max_length = 40,default='')
	score = models.IntegerField()

	def __str__(self):
		return '{} {} {}'.format(self.name, self.email_address, self.score)

class Manager(models.Model):
	name = models.CharField(max_length = 30)
	email_address = models.CharField(max_length = 40)

	def __str__(self):
		return '{} {}'.format(self.name, self.email_address)