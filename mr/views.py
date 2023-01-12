from django.shortcuts import render, redirect

from django.views import generic # for service detail view

# for search/paginator
from django.db.models import Q
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404

# my addition
from django.http import HttpResponse

from .models import Employee, Status, Division, Property, Service
from .forms import EmployeeForm, PropertyForm, ServiceForm

def index(request):
#	return render(request, 'members/base.html')
    return render(request, 'mr/home.html')


def employee_list(request):
    #if request.user.is_superuser:
    if request.user.groups.filter(name='App_Admin').exists():
        context = {'employee_list':Employee.objects.all()}
    else:
        context = {'employee_list':Employee.objects.filter(user=request.user)}
    return render(request, 'mr/employee_list.html', context)


# new record / update record
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=emp)
        return render(request,'mr/employee_form.html',{'form':form})
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


# new/update Property record FORM
def PropertyForms(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PropertyForm()
        else:
            property = Property.objects.get(pk=id)
            form = PropertyForm(instance=property)
        return render(request,'mr/property_form.html',{'form':form})
    else:
        if id == 0:
            form = PropertyForm(request.POST)
        else:
            property = Property.objects.get(pk=id)
            form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
        return redirect('property_list')


def PropertyList(request):
 #   context = {'property_list':Property.objects.all()}
 #   return render(request, 'mr/property_list.html', context)

    #if request.user.is_superuser:
    if request.user.groups.filter(name='App_Admin').exists():
        context = {'property_list':Property.objects.all()}
    else:
        context = {'property_list':Property.objects.filter(user__user=request.user)}
    return render(request, 'mr/property_list.html', context)
#user table and user relationship


def PropertyDelete(request,id):
    property = property.objects.get(pk=id)
    property.delete()
    return redirect('property_list')


# service module
def ServiceList(request):
    #if request.user.is_superuser:
    if request.user.groups.filter(name='App_Admin').exists():
        context = {'service_list':Service.objects.all()}
        #context = {'service_list':Service.objects.order_by('prop__serial_no').distinct('prop__serial_no')}
        #context = {'service_list':Service.objects.filter('prop__serial_no').values('prop__property_no').distinct().last().get('prop__property_no')}
    else:
        context = {'service_list':Service.objects.filter(prop__user__user=request.user)}
    return render(request, 'mr/service_list.html', context)


# new/update Service record FORM
def ServiceForms(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ServiceForm()
        else:
            service = Service.objects.get(pk=id)
            form = ServiceForm(instance=service)
        return render(request,'mr/service_form.html',{'form':form})
    else:
        if id == 0:
            form = ServiceForm(request.POST)
        else:
            service = Service.objects.get(pk=id)
            form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
        return redirect('service_list')


def ServiceDelete(request,id):
    service = Service.objects.get(pk=id)
    service.delete()
    return redirect('service_list')

# test detail view (class)
class ServiceDetailView(generic.DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'mr/service_detail.html'

# dec 7 list/searc/paginator
def PropertyService(request):
    property_service_list = Property.objects.all()

    query = request.GET.get("q")
    if query:
        property_service_list = property_service_list.filter(
                Q(user__icontains=query)|
                Q(asset_type__icontains=query)
            )
    paginator = Paginator(property_service_list, 2) # show 2 per page
    page = request.GET.get('page')
    propservpages = paginator.get_page(page)
    return render(request, 'mr/propertyserv_detail.html', {'propservpages': propservpages})


def PropertyServiceDetail(request, id):
    propservdet = get_object_or_404(Property, pk=id)
    return render(request, 'mr/showpropserv_details.html', {'propservdet':propservdet})

# dec 16
class PropertyDetailView(generic.DetailView):
    model = Property
    context_object_name = 'my_property'
    template_name = 'mr/service_detail2.html'



# not working (below this line)
def ServiceProperty(request):
#    service_property_list = Service.objects.all().distinct('prop_id')
#    service_property_list = Service.objects.values('propservice.serial_no')
    service_property_list = Service.objects.all()
#    service_property_list = Service.objects.values().order_by('serial_no')

    query = request.GET.get("q")
    if query:
        service_property_list = service_property_list.filter(
                Q(user__icontains=query)|
                Q(asset_type__icontains=query)
            )
    paginator = Paginator(service_property_list, 5) # show 5 per page
    page = request.GET.get('page')
    servproppages = paginator.get_page(page)
    return render(request, 'mr/servprop_detail.html', {'servproppages': servproppages})


def ServPropDetail(request, id):
    servpropdetpages = get_object_or_404(Service, pk=id)
    return render(request, 'mr/showservprop_detail.html', {'servpropdetpages':servpropdetpages})


# Dec 13

class ServiceListView(generic.ListView):
    model = Service
    #paginate_by = 2
    template_name = 'mr/service_list2.html'  # deleted


class PropertyListView(generic.ListView):
    model = Property 
    context_object_name = 'property'
    template_name = 'mr/property_detail2.html' # deleted


# class ServiceDetailView(generic.DetailView):
#     model = Service
#     context_object_name = 'service'
#     template_name = 'mr/service_detail2.html'     # deleted

def ServiceDetail(request, id):
    serviceD = get_object_or_404(Service, pk=id)
    return render(request, 'mr/service_detail2.html', {'serviceD':serviceD}) # view deleted


#Dec 15
def all_property(request):
    propList = Property.objects.all()
    servList = Service.objects.all()

    return render(request, 'mr/all_property.html', {'propList':propList, 'servList':servList})


#Dec 17 MR report/view module  -- working
def MrList(request):
    if request.user.groups.filter(name='App_Admin').exists():
        employee_list = Employee.objects.all()
        query = request.GET.get("q")
        if query:
            employee_list = employee_list.filter(
                Q(lastname__icontains=query)|
                Q(division__icontains=query)
                )
        paginator = Paginator(employee_list, 2) # show 2 per page
        page = request.GET.get('page')
        emppages = paginator.get_page(page)
    else:
    #    context = {'service_list':Service.objects.filter(prop__user__user=request.user)}
        employee_list = Employee.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            employee_list = employee_list.filter(
                Q(lastname__icontains=query)|
                Q(division__icontains=query)
                )
        paginator = Paginator(employee_list, 2) # show 2 per page
        page = request.GET.get('page')
        emppages = paginator.get_page(page)
    return render(request, 'mr/mrlist.html', {'emppages':emppages})


def MrDetail(request, id):
    emp = get_object_or_404(Employee, pk=id)
    return render(request, 'mr/mrdetail.html', {'emp':emp})

#end Dec 17

# Dec 18
# def ServicePropertyDetail(request, id):
# #    serviceprop = get_object_or_404(Service, pk=id)
#     serviceprop = get_object_or_404(Service, pk=id)
#     return render(request, 'mr/service_detail2.html', {'serviceprop':serviceprop})


def ServicePropertyDetail(request, id):
#    serviceprop = get_object_or_404(Service, pk=id)
    serviceprop = get_object_or_404(Property, pk=id)
    return render(request, 'mr/service_detail2.html', {'serviceprop':serviceprop})

# to move to employee group
def Employee_Detail(request, id):
    empDet = get_object_or_404(Employee, pk=id)
    return render(request, 'mr/employee_detail.html', {'empDet':empDet})




