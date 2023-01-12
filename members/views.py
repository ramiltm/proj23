from django.shortcuts import render, redirect


# my addition
from django.http import HttpResponse

from .models import Employee, Status, Division
from .forms import EmployeeForm

def index(request):
#	return render(request, 'members/base.html')
    return render(request, 'members/home.html')


def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, 'members/employee_list.html', context)


# new record / update record
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=emp)
        return render(request,'members/employee_form.html',{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_delete(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('employee_list')


# class EmployeeDeleteView(DeleteView):
#     model = Employee
#     template_name = 'delete_employee_view.html'
#     success_url = reverse_lazy('employee_list')


# def detail(request, id):
#     emp = get_object_or_404(employee, pk=id)
#     return render(request, 'assMngt/emp_mrdetails.html', {'emp':emp})