from django.db import models



class Employee(models.Model):
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True) 
    employee_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)  # Ensure this exists

    def __str__(self):
        return self.employee_name
    class Meta:
        db_table = 'employee_list'



class EmailID(models.Model):
    BRANCH_CHOICES = [
        ('Khobar', 'Khobar'),
        ('Riyadh', 'Riyadh'),
        ('Jeddah', 'Jeddah'),
    ]

    employee_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    old_pass = models.CharField(max_length=100)
    new_pass = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, default='Khobar')
    

    def __str__(self):
        return self.email_id

    class Meta:
        db_table = 'employee_EmailID'



class Device(models.Model):
    BRANCH_CHOICES = [
        ('Khobar', 'Khobar'),
        ('Riyadh', 'Riyadh'),
        ('Jeddah', 'Jeddah'),
    ]

    employee_name = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, default='Khobar')

    def __str__(self):
        return self.device_name

    class Meta:
        db_table = 'employee_device' 

class Server(models.Model):
    BRANCH_CHOICES = [
        ('Khobar', 'Khobar'),
        ('Riyadh', 'Riyadh'),
        ('Jeddah', 'Jeddah'),
    ]

    server_type = models.CharField(max_length=100)
    server_name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, default='Khobar')

    def __str__(self):
        return self.server_name

    class Meta:
        db_table = 'employee_Server' 
    

