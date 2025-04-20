
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),  # Make sure this line is present
    path('students/', include(('students.urls', 'students'), namespace='students')),
]
