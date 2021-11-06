from django.db import models

# Create your models here.
class Images(models.Model):
	img = models.ImageField(verbose_name='Imagen',upload_to = 'image/', null=True, blank=True)



class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=30)

class SendMail(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	message = models.CharField(max_length = 50)
	to_email = models.CharField(max_length=30)