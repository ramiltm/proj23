from django.contrib import admin

# Register your models here.
from .models import (
	Employee, Division, Status
	)

admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(Status)
