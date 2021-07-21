from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('Full_Name', 'Mobile_Number', 'Employee_Code', 'Position')
        labels = {
            'Full_Name': 'Full Name',
            'Mobile_Number': 'Mobile Number',
            'Employee_Code': 'Employee Code',
            'Position': 'Position',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, *kwargs)
        self.fields['Position'].empty_label = "Select"
