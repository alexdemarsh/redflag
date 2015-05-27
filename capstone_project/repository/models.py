from django.db import models


# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class Data(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	owner = models.ForeignKey(User, related_name='%(class)s_requests_created')
	users = models.ManyToManyField(User)
	url = models.URLField(default='')
	version = models.IntegerField(default=1)

	def __str__(self):
		return self.name

class Math(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	LANGUAGES = (
		('R', 'R'), 
		('Python', 'Python'), 
		('SAS', 'SAS'), 
		('STATA', 'STATA'), 
		('Julia', 'Julia'),
	)
	language = models.CharField(max_length = 10, choices=LANGUAGES)
	owner = models.ForeignKey(User, related_name='%(class)s_requests_created')
	users = models.ManyToManyField(User)
	related_data = models.ManyToManyField(Data, related_name='%(class)s_requests_created')
	code = models.TextField()
	version = models.IntegerField()

	def __str__(self):
		return self.name

# class Alert(models.Model):
#	name = models.CharField()
# 	origin = models.ForeignKey(Math)
# 	sent_on = models.DateTimeField(auto_now_add=True)	
# 	destination = models.ForeignKey(User)	

#	def __str__(self):
#		reutn self.name