from django.contrib import admin

# Register your models here.
from .models import (
	Employee, Division, Status, Equipment, PropertyOfficer, IT_Officer,
	Property, Service
	)

admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(Status)

admin.site.register(Property)
admin.site.register(Equipment)
admin.site.register(PropertyOfficer)

admin.site.register(IT_Officer)
admin.site.register(Service)