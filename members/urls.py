from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),

	path('new_employee', views.employee_form, name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), #get and post req. for update operatoion
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
 #   path('delete/<int:id>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee_list', views.employee_list, name='employee_list'), # get req. to retrieve and display all records.

# view/report
  # 	path('emp/<id>/', views.detail, name='detail'),
]