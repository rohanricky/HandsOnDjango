from django.db import models
from django.forms import forms

class Feedback(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.CharField(max_length=100)

    def __str__(self):
    	return self.subject,self.message,self.sender

class signin(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return [self.username,self.password]