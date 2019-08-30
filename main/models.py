from django.db import models

# Create your models here.
class Country(models.Model):

	id = models.AutoField(primary_key=True)
	country_name = models.CharField(null=False, blank=False ,max_length=100)

class Ip(models.Model):
	
	id = models.AutoField(primary_key=True)
	ip = models.CharField(null=False, blank=False ,max_length=100)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

class Date(models.Model):
	
	id = models.AutoField(primary_key=True)
	date = models.CharField(null=False, blank=False ,max_length=100)

class File(models.Model):

	id = models.AutoField(primary_key=True)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
	date = models.ForeignKey('Date', on_delete = models.SET_NULL, null = True)
	ip = models.ForeignKey('Ip', on_delete = models.SET_NULL, null = True)
	file_name = models.CharField(max_length=500)
	file_path = models.FileField(upload_to='data/%Y/%m/%d/')

class Voip(models.Model):

	id = models.AutoField(primary_key=True)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
	date = models.ForeignKey('Date', on_delete = models.SET_NULL, null = True)
	ip = models.ForeignKey('Ip', on_delete = models.SET_NULL, null = True)
	file_name= models.CharField(max_length=500)
	file_path = models.FileField(upload_to='data/%Y/%m/%d/')

class Url(models.Model):

	id = models.AutoField(primary_key=True)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
	date = models.ForeignKey('Date', on_delete = models.SET_NULL, null = True)
	ip = models.ForeignKey('Ip', on_delete = models.SET_NULL, null = True)
	url = models.TextField()

class Cred(models.Model):

	id = models.AutoField(primary_key=True)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
	date = models.ForeignKey('Date', on_delete = models.SET_NULL, null = True)
	ip = models.ForeignKey('Ip', on_delete = models.SET_NULL, null = True)
	cred = models.TextField()
	
class Dns(models.Model):

	id = models.AutoField(primary_key=True)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
	date = models.ForeignKey('Date', on_delete = models.SET_NULL, null = True)
	ip = models.ForeignKey('Ip', on_delete = models.SET_NULL, null = True)
	dns = models.TextField()