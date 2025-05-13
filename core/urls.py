from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('student/', include('student.urls')),
    path('application/', include('application.urls')),
    path('employee/', include('employee.urls')),
]
