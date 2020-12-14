from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Customer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __str__(self):
		return self.first_name + ' ' + self.last_name 
        