from django.db import models

# Create your models here.

class Country(models.Model):
	country_name = models.CharField(max_length=200)
	def __str__(self):
		return self.country_name

class City(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	city_name = models.CharField(max_length=200)
	def __str__(self):
		return self.city_name

class Visit(models.Model):
	region_visited = models.ManyToManyField(City)
	visit_date = models.DateTimeField('date visited')
	article = models.CharField(max_length=2000)
