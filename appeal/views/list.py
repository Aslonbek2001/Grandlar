from django.views.generic import ListView
from django.shortcuts import redirect
from appeal.models import Appeal
from users.models import User

class AppealListView(ListView):
    model = Appeal
    template_name = 'appeal/list.html'
    context_object_name = 'appeals'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'student':
                # Student faqat o'z apelatsiyalarini ko'radi
                return Appeal.objects.filter(student__user=user)
            elif user.role == 'training' or user.role == 'spirituality' or user.role == 'special':
                # Expert barcha apelatsiyalarni ko'radi
                return Appeal.objects.all()
        return Appeal.objects.none()