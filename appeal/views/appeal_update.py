from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from appeal.models import Appeal, AppealConditions
from appeal.forms import AppealForm
from application.models import Application
from student.models import Student
from django.contrib import messages
from django.shortcuts import redirect

class AppealUpdateView(LoginRequiredMixin, UpdateView):
    model = Appeal
    form_class = AppealForm
    template_name = 'appeal/update.html'
    success_url = reverse_lazy('main:index')

    def dispatch(self, request, *args, **kwargs):
        if not self.is_within_appeal_period():
            messages.error(request, "Hozirda apelatsiyani tahrirlash mumkin emas.")
            return redirect('main:index')

        if not self.application_check():
            messages.error(request, "Siz hali ariza topshirmagansiz, shuning uchun apelatsiyani tahrirlash mumkin emas.")
            return redirect('main:index')

        appeal = self.get_object()
        if appeal.student.user != request.user:
            messages.error(request, "Siz ushbu apelatsiyani tahrirlash huquqiga ega emassiz.")
            return redirect('main:index')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Apelatsiyangiz muvaffaqiyatli yangilandi.")
        return super().form_valid(form)

    def is_within_appeal_period(self):
        today = timezone.now().date()
        return AppealConditions.objects.filter(start_date__lte=today, end_date__gte=today).exists()

    def application_check(self):
        student = Student.objects.get(user=self.request.user)
        today = timezone.now().date()
        return Application.objects.filter(student=student, created_at__year=today.year).exists()