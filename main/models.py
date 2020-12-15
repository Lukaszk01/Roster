from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)


class Customer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __str__(self):
		return self.first_name + ' ' + self.last_name 
        