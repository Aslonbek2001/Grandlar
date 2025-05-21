from django.views.generic import ListView
from application.models import Application, ApplicationStatus

class ApplicationListView(ListView):
    model = Application
    template_name = 'application/list.html'
    context_object_name = 'applications' 
    
    def get_queryset(self):
        user = self.request.user

        if user.role == 'student':
            # Talaba faqat o‘z arizalarini ko‘radi
            return Application.objects.filter(student=user.profile)
        
        elif user.role == 'training':
            # Manager faqat yangi arizalarni ko‘radi
            return Application.objects.filter(application_status=ApplicationStatus.NEW)

        elif user.role == 'spirituality':
            # Admin barcha arizalarni ko‘radi
            return Application.objects.all()
        
        elif user.role == 'special':
            # Admin barcha arizalarni ko‘radi
            return Application.objects.all()







