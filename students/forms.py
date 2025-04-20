from django import forms
from .models import Employee, EmailID, Device, Server



class EmployeeForm(forms.ModelForm):
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('Finance', 'Finance'),
    ]
    
    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Intern', 'Intern'),
    ]

    BRANCH_CHOICES = [
        ('Khobar', 'Khobar'),
        ('Jeddah', 'Jeddah'),
        ('Riyadh', 'Riyadh'),
    ]

    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    position = forms.ChoiceField(choices=POSITION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ChoiceField(choices=BRANCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    employee_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['employee_name', 'department', 'position', 'branch']


class EmailIDForm(forms.ModelForm):
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('Finance', 'Finance'),
    ]

    BRANCH_CHOICES = [
        ('Khobar', 'Khobar'),
        ('Riyadh', 'Riyadh'),
        ('Jeddah', 'Jeddah'),
    ]

    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ChoiceField(choices=BRANCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = EmailID
        fields = ['employee_name', 'email_id', 'department', 'position', 'old_pass', 'new_pass', 'branch']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'old_pass': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_pass': forms.PasswordInput(attrs={'class': 'form-control'}),
           
        }


class DeviceForm(forms.ModelForm):
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('Finance', 'Finance'),
    ]

    BRANCH_CHOICES = [
        ('Khobar', 'Khobar'),
        ('Jeddah', 'Jeddah'),
        ('Riyadh', 'Riyadh'),
    ] 

    
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ChoiceField(choices=BRANCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Device
        fields = ['employee_name', 'device_name', 'department', 'username', 'password']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'device_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class ServerForm(forms.ModelForm):
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('Finance', 'Finance'),
    ]

    BRANCH_CHOICES = [
        ('Khobar', 'Khobar'),
        ('Jeddah', 'Jeddah'),
        ('Riyadh', 'Riyadh'),
    ] 

    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ChoiceField(choices=BRANCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Server
        fields = ['server_type', 'server_name', 'ip_address', 'username', 'password']
        widgets = {
            'server_type': forms.TextInput(attrs={'class': 'form-control'}),
            'server_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        
        }


