import random
from django.test import TestCase
from .models import Employee  

class EmployeeModelUnitTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            department='IT',
            employee_name='Bob Smith',
            computer_name='Laptop-01',
            cpu_hilti_number='1234567890',
            sn_number_monitor='SN12345678',
            monitor_hilti_number='9876543210',
            service_tag='TAG123456',
            configuration='Intel i7, 16GB RAM, 512GB SSD'
        )

    def test_employee_model(self):
        data = self.employee
        self.assertIsInstance(data, Employee)
        self.assertEqual(data.department, 'IT')
        self.assertEqual(data.employee_name, 'Bob Smith')

