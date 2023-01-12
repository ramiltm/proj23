from django.urls import path

from . import views

urlpatterns = [
	path('create-pdf/<int:id>', views.create_pdf_report, name='create-pdf'),
	path('create-csv-report/<int:id>', views.create_csv_report, name='create-csv-report'),

	path('create_pdf_service/<int:id>', views.create_pdf_service, name='create_pdf_service'),
]