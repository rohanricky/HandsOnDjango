# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class SignIn(models.Model):
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.email,self.password


