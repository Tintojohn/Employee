from django.shortcuts import render,redirect
from .models import *
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    return render(request, "emp_register/employee_list.html")

def employee_form(request):
    if request.method=='GET':
        form = EmployeeForm()
        return render(request, "emp_register/employee_form.html", {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')

def employee_delete(request):
    return
