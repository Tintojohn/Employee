from django.shortcuts import render, redirect
from .models import *
from .forms import EmployeeForm
from django.http import HttpResponse

# Create your views here.

def employee_list(request):
    emp_list = Employee.objects.all()
    return render(request, "emp_register/employee_list.html", {'emp_list': emp_list})

def employee_form(request,id):
    if request.method == 'GET':
        emp = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=emp)
        return render(request, "emp_register/update.html", {'form': form})
    else:
        emp = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/list')

def insert(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, "emp_register/employee_form.html", {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_delete(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('/list')
