from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('empty/', views.empty_page, name='dashboard'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee/<int:id>/', views.view_employee, name='view_employee'),
    path('employee/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('search_employee/', views.search_employee, name='search_employee'),

    path('add_email_id/', views.add_email_id, name='add_email_id'),
    path('email_id_list/<str:branch>/', views.email_id_list, name='email_id_list'),
    path('edit_email_id/<int:id>/', views.edit_email_id, name='edit_email_id'),
    path('delete_email_id/<int:id>/', views.delete_email_id, name='delete_email_id'),
    
    path('add_device/<str:branch>/', views.add_device, name='add_device'),
    path('edit_device/<int:id>/', views.edit_device, name='edit_device'),  # ✅ Fixed name
    path('delete_device/<int:id>/', views.delete_device, name='delete_device'),
    path('device_id_list/<str:branch>/', views.device_list_branch, name='device_list_branch'),  # ✅ Removed extra `/`


 
    path('server-details/', views.server_details_branch, name='server_details'),
    path('servers/<str:branch>/', views.server_details_branch, name='server_details_branch'),
    path('add-server/<str:branch>/', views.add_server_view, name='add_server'),
    path('edit-server/<int:server_id>/', views.edit_server_view, name='edit_server'),
    path('delete-server/<int:server_id>/', views.delete_server_view, name='delete_server'),
    path('servers/branch/<str:branch>/', views.server_details_branch, name='server_list_branch'), 
    
]
