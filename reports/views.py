from django.shortcuts import render
# Create your views here.
from mr.models import Employee, Property

# for pdf
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa
# for csv
from django.template import loader, Context

import csv

from reports.utils import render_to_pdf

def create_pdf_report(request, id):
	empDet = get_object_or_404(Employee, pk=id)
	template_path = 'reports/emp_reportpdf.html'
	context = {'empDet':empDet}
	# Create a Django response object, and specify contnet_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# to dowloand
	#response['Content-Disposition'] = 'attachment; filename="emp_report.pdf"'
	# to open to browser remove attachment
	response['Content-Disposition'] = 'filename="emp_report.pdf"'
	# find the template and render it.
	template = get_template(template_path)
	html = template.render(context)

	# create a pdd
	pisa_status = pisa.CreatePDF(
		html, dest=response)
	# if error then show some funny view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response


# def create_csv_report(request, id):
# 	empDet = get_object_or_404(Employee, pk=id)
# 	template_path = 'reports/emp_reportpdf.html'
# 	context = {'empDet':empDet}
# 	# Create a Django response object, and specify contnet_type as pdf
# 	response = HttpResponse(content_type='text/csv')
# 	# to dowloand
# 	response['Content-Disposition'] = 'attachment; filename="emp_report.csv"'
# 	# to open to browser remove attachment
# 	#response['Content-Disposition'] = 'filename="emp_report.pdf"'
# 	# find the template and render it.
# 	template = get_template(template_path)
# 	html = template.render(context)

# 	# create a pdd
# 	pisa_status = pisa.CreatePDF(
# 		html, dest=response)
# 	# if error then show some funny view
# 	if pisa_status.err:
# 		return HttpResponse('We had some errors <pre>' + html + '</pre>')
# 	return response

# working for all records
def create_csv_report(request,id):
	employees = Employee.objects.all()
	#employees = Employee.objects.all().values_list('id', flat=True)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="empcsv_report.csv"'

	writer = csv.writer(response)
	writer.writerow(['firstname', 'lastname', 'middleI', 'division', 'position', 'empStatus'])
	emps = employees.values_list('firstname', 'lastname', 'middleI', 'division', 'position', 'empStatus')

	for emp in emps:
		writer.writerow(emp)
	return response

######## sample
# def export_users_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="users.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['employee','IG', 'follower', 'email', 'website', 'DA', 'youtube_url', 'youtube_name', 'subscriber', 'type','country'])

#     users = Library.objects.all().values_list('employee','IG', 'follower', 'email', 'website', 'DA', 'youtube_url', 'youtube_name', 'subscriber', 'type','country')
#     for user in users:
#         writer.writerow(user)

#     return response

# urls.py
# from .views import export_users_csv

# path('export', export_users_csv, name='export_users_csv'),
#page.html
# <a href="{% url 'export_users_csv' %}">Export all users</a>
################ end sample

##### Dec 27: Services to pdf
def create_pdf_service(request, id):
	serviceprop = get_object_or_404(Property, pk=id)
	template_path = 'reports/service_pdfreport.html'
	context = {'serviceprop':serviceprop}
	# Create a Django response object, and specify contnet_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# to dowloand
	#response['Content-Disposition'] = 'attachment; filename="emp_report.pdf"'
	# to open to browser remove attachment
	response['Content-Disposition'] = 'filename="service_report.pdf"'
	# find the template and render it.
	template = get_template(template_path)
	html = template.render(context)

	# create a pdd
	pisa_status = pisa.CreatePDF(
		html, dest=response)
	# if error then show some funny view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response

