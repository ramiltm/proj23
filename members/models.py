from django.db import models

# Create your models here.

# lookup table for employee
class Division(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Status(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "status"


class Employee(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	middleI = models.CharField(max_length=2)
	division = models.ForeignKey(Division, related_name='empdiv',on_delete=models.SET_NULL, null=True)
	position = models.CharField(max_length=30)
	empStatus = models.ForeignKey(Status, related_name='empstat',on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return '{}, {} {}'.format(
			self.lastname, self.firstname, self.middleI
			)