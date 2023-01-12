from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index, name='index'),

	path('new_employee', views.employee_form, name='employee_insert'), # get and post req. for insert operation
  path('<int:id>/', views.employee_form, name='employee_update'), #get and post req. for update operatoion
  path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
 #   path('delete/<int:id>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
  path('employee_list', views.employee_list, name='employee_list'), # get req. to retrieve and display all records.

# view/report
  # 	path('emp/<id>/', views.detail, name='detail'),

# mr property
  path('new_property', views.PropertyForms, name='property_insert'),
  path('property_list', views.PropertyList, name='property_list'),
  path('property/<int:id>/', views.PropertyForms, name='property_update'),
  path('delete/<int:id>/', views.employee_delete, name='property_delete'),

# service
  path('service_list', views.ServiceList, name='service_list'),
  path('service', views.ServiceForms, name='service'),
  path('service/<int:id>/', views.ServiceForms, name='service_update'),
  path('delete/<int:id>/', views.ServiceDelete, name='service_delete'),

# test
  path('service_detail/<int:id>/', views.ServiceDetailView.as_view(), name='service_detail'),  # test detail view(class)

  path('propserv/', views.PropertyService, name='propserv'),
  path('propserv/<id>', views.PropertyServiceDetail, name='propservdetail'),

  path('servprop/', views.ServiceProperty, name='servprop'),
#  path('servprop/', views.ServiceProperty, name='servprop'),
  path('servprop/<id>', views.ServPropDetail, name='servpropdetail'),

# dec 13
#  path('service_detail/<id>', views.ServiceDetailView.as_view(), name='service_detail'),  # test detail view(class)
  path('service_list2/', views.ServiceListView.as_view(), name='service_list2'),


  path('property_detail2/', views.PropertyListView.as_view(), name='property_detail2'),
  path('service_detail2/<int:id>', views.ServiceDetail, name='service_detail2'),

# dec 15
  path('all_property/', views.all_property, name='all_property'),

# dec 16
  path('my_property/<int:pk>/', views.PropertyDetailView.as_view(), name='my_property'),
  
# view/report
  path('issued_property/', views.MrList, name='issued_property'),
  #path('issued_property/<id>/', views.MrList, name='issued_property'),
  path('issued_property_detail/<id>/', views.MrDetail, name='issued_property_detail'),

# dec 18 to be move up
  path('service_propDetail/<id>/', views.ServicePropertyDetail, name='service_propDetail'),
# move to employee group
  path('employee_detail/<id>/', views.Employee_Detail, name='employee_detail'),
]