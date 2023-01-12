from django.db import models

# Create your models here.
from django.contrib.auth.models import User

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
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	middleI = models.CharField(max_length=2)
	division = models.ForeignKey(Division, related_name='empdiv',on_delete=models.SET_NULL, null=True)
	profstatus = models.CharField(max_length=30, null=True)
	position = models.CharField(max_length=30)
	empStatus = models.ForeignKey(Status, related_name='empstat',on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return '{}, {} {}'.format(
			self.lastname, self.firstname, self.middleI
			)

# lookup table for property
class Equipment(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name


class PropertyOfficer(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)

	def __str__(self):
		return '{}, {}'.format(
			self.lastname, self.firstname
			)


class Property(models.Model):
#	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user = models.ForeignKey(Employee, related_name='emps', on_delete=models.SET_NULL, null=True)
	asset_type = models.ForeignKey(Equipment, related_name='equips', on_delete=models.SET_NULL, null=True)
	unit_office = models.CharField(max_length=10, default='BLGF')
	decription = models.CharField(max_length=100)
	property_no = models.CharField(max_length=50)
	serial_no = models.CharField(max_length=20)
	year_acquired = models.CharField(max_length=5)
	issued_to = models.ForeignKey(Employee, related_name='emp_tos', on_delete=models.SET_NULL, null=True)
	issued_by = models.ForeignKey(PropertyOfficer, related_name='propoff', on_delete=models.SET_NULL, null=True)
	original_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name = 'Original Value')
	#useful_life = models.DateField('Useful Life')
	useful_life = models.IntegerField()
	salvage_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name = 'Salvage Value')

	def __str__(self):
		return '{}, {}'.format(
			self.property_no, self.serial_no
			)


class IT_Officer(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)

	def __str__(self):
		return '{}, {}'.format(
			self.lastname, self.firstname
			)

class Service(models.Model):
	prop = models.ForeignKey(Property, related_name='propservice', on_delete=models.SET_NULL, null=True)
	date = models.DateField()
	issues = models.CharField(max_length=100)
	service_rendered = models.CharField(max_length=50)
	action_officer =  models.ForeignKey(IT_Officer, related_name='servOff', on_delete=models.SET_NULL, null=True)
	remarks = models.CharField(max_length=150)

	def __str__(self):
		return self.issues
