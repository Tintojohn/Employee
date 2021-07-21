from .models import Employee
from django import forms

class EmployeeForm(forms.Form):
    class meta:
        model = Employee
        fields = ('Full_Name', 'Mobile_Number', 'Employee_Code', 'Position')
        labels = {
            'Full_Name': 'Full Name',
            'Mobile_Number': 'Mobile Number',
            'Employee_Code': 'Employee Code'
        }