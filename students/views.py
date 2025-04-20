from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import EmployeeForm, EmailIDForm, DeviceForm, ServerForm
from .models import Employee, EmailID, Device, Server
from django.contrib import messages
from django.http import Http404


def employee_list(request):
    employees = Employee.objects.all()  
    context = {
        'employees': employees
    }
    return render(request, 'students/employee_list.html', context)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list') 
    else:
        form = EmployeeForm()

    return render(request, 'students/add_employee.html', {'form': form})


def index(request):
    return render(request, 'students/index.html')


def view_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'students/view_employee.html', {'employee': employee})


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'students/edit_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')  


def search_employee(request):
    query = request.GET.get('q', '')
    employees = Employee.objects.filter(employee_name__icontains=query)
    return render(request, 'students/index.html', {'employees': employees})





def add_email_id(request):
    if request.method == 'POST':
        form = EmailIDForm(request.POST)
        if form.is_valid():
            email_id = form.save()
            messages.success(request, "Email ID added successfully!")
            
            
            branch = email_id.branch
            redirect_url = reverse('email_id_list', kwargs={'branch': branch})
            print(f"Redirecting to: {redirect_url}")  
            
            return redirect(redirect_url)
        else:
            print("Form errors:", form.errors)  
            messages.error(request, "Failed to add Email ID. Please check the form.")
    else:
        form = EmailIDForm()
    
    return render(request, 'students/add_email_id.html', {'form': form})





def edit_email_id(request, id):
    email_id = get_object_or_404(EmailID, id=id)
    branch = email_id.department  
    
    if request.method == 'POST':
        form = EmailIDForm(request.POST, instance=email_id)
        if form.is_valid():
            form.save()
            return redirect('email_id_list', branch=branch)  
    else:
        form = EmailIDForm(instance=email_id)
    
    return render(request, 'students/edit_email_id.html', {'form': form, 'branch': branch})


def delete_email_id(request, id):
    email_id = get_object_or_404(EmailID, id=id)
    branch = email_id.department  
    email_id.delete()
    messages.success(request, "Email ID deleted successfully!")  
    return redirect('email_id_list', branch=branch)


def email_id_list(request, branch):
  
    email_ids = EmailID.objects.filter(branch=branch)
    
   
    if branch == 'Khobar':
        template_name = 'students/email_id_list_khobar.html'
    elif branch == 'Riyadh':
        template_name = 'students/email_id_list_Riyadh.html'
    elif branch == 'Jeddah':
        template_name = 'students/email_id_list_jeddah.html'
    else:
        template_name = 'students/email_id_list.html' 
    
    context = {
        'email_ids': email_ids
    }
    
    return render(request, template_name, context)




def add_device(request, branch):
    form = DeviceForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        new_device = form.save(commit=False)
        new_device.branch = branch  
        new_device.save()
        messages.success(request, "Device added successfully!")
        return redirect('device_list_branch', branch=branch)

    return render(request, 'students/add_device.html', {'form': form, 'branch': branch})


def edit_device(request, id):
    device = get_object_or_404(Device, id=id)
    branch = device.branch
    
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, "Device updated successfully!")
            return redirect('device_list_branch', branch=branch)
    else:
        form = DeviceForm(instance=device)
    
    return render(request, 'students/edit_device.html', {'form': form, 'branch': branch})


def delete_device(request, id):
    device = get_object_or_404(Device, id=id)
    branch = device.branch
    device.delete()
    messages.success(request, "Device deleted successfully!")
    return redirect('device_list_branch', branch=branch)


def device_list_branch(request, branch):
    # Normalize branch names to match your template file names
    branch_templates = {
        'Khobar': 'students/device_list_khobar.html',
        'Riyadh': 'students/device_list_Riyadh.html',
        'Jeddah': 'students/device_list_jeddah.html'
    }

    # Select the correct template based on branch, otherwise use default
    template_name = branch_templates.get(branch, 'students/device_list_branch.html')

    # Fetch devices for the selected branch
    devices = Device.objects.filter(branch=branch)

    context = {
        'devices': devices,
        'branch': branch
    }

    return render(request, template_name, context)


def add_server_view(request, branch):
    form = ServerForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        server = form.save(commit=False)
        server.branch = branch  
        server.save()
        messages.success(request, 'Server added successfully!')
        return redirect('server_details_branch', branch=branch)

    context = {
        'form': form,
        'branch': branch,
    }
    return render(request, 'students/add_server.html', context)



def edit_server_view(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    branch = server.branch
    
    if request.method == 'POST':
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            messages.success(request, "Server updated successfully.")
            return redirect('server_details_branch', branch=branch)
    else:
        form = ServerForm(instance=server)

    return render(request, 'students/edit_server.html', {'form': form, 'branch': branch})



def delete_server_view(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    if request.method == 'POST':
        server.delete()
        messages.success(request, 'Server deleted successfully.')
        return redirect('server_details_branch', branch=server.branch)
    return render(request, 'students/delete_server.html', {'server': server})









def server_details_branch(request, branch):
    valid_branches = ['Khobar', 'Riyadh', 'Jeddah']
    if branch not in valid_branches:
        return HttpResponse("Invalid branch", status=404)

    servers = Server.objects.filter(branch=branch)
    context = {
        'servers': servers,
        'branch': branch,
    }
    return render(request, 'students/server_details.html', context)



def empty_page(request):
    total_employees = Employee.objects.count()
    total_devices = Device.objects.count()
    total_emails = EmailID.objects.count()
    total_servers = Server.objects.count()


    context = {
        'total_employees': total_employees,
        'total_devices': total_devices,
        'total_emails': total_emails,
        'total_servers': total_servers,

    }
    return render(request, 'students/empty_page.html', context)
