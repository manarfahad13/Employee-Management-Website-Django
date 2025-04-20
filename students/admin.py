from django.contrib import admin
from .models import Employee, EmailID, Device

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'employee_name', 'branch')  # Removed non-existent fields
    search_fields = ('department', 'employee_name', 'branch')  # Removed non-existent fields


@admin.register(EmailID)
class EmailIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_name', 'email_id', 'department', 'position', 'old_pass', 'new_pass')
    search_fields = ('employee_name', 'email_id', 'department', 'position')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_name', 'device_name', 'department', 'username', 'password')
    search_fields = ('employee_name', 'device_name', 'department', 'username')
