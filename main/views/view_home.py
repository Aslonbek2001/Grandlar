from django.shortcuts import render
from application.models import Application

def index(request):
    data = {
        'students_count': 1980,
        'applications_count': Application.objects.all().count(),
        'approved_applications': Application.objects.filter(application_status='approved').count(),
        'rejected_applications': Application.objects.filter(application_status='rejected').count()
    }
    return render(request, 'result/index.html', context=data)
