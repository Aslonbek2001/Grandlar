from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from appeal.models import Appeal, AppealConditions
from appeal.forms import AppealForm
from application.models import Application
from student.models import Student
from django.contrib import messages
from django.shortcuts import redirect

class AppealCreateView(LoginRequiredMixin, CreateView):
    model = Appeal
    form_class = AppealForm
    template_name = 'appeal/appeal_create.html'
    success_url = reverse_lazy('main:index')

    def dispatch(self, request, *args, **kwargs):
        # 1️⃣ Vaqt tekshirish
        if not self.is_within_appeal_period():
            messages.error(request, "Hozirda apelatsiya yuborish mumkin emas.")
            return redirect('main:index')

        # 2️⃣ Student ariza topshirganmi tekshirish
        if not self.application_check():
            messages.error(request, "Siz hali ariza topshirmagansiz, shuning uchun apelatsiya yubora olmaysiz.")
            return redirect('main:index')

        # 3️⃣ Bu yil apelatsiya yuborganmi?
        if self.has_already_appealed_this_year():
            messages.error(request, "Siz bu yil allaqachon apelatsiya yuborgansiz.")
            return redirect("appeal:appeal_list")
        
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            student = Student.objects.get(user=self.request.user)
            form.instance.student = student
            messages.success(self.request, "Apelatsiyangiz muvaffaqiyatli yuborildi.")
            return super().form_valid(form)
        except Student.DoesNotExist:
            form.add_error(None, "Talaba topilmadi.")
            return self.form_invalid(form)
        
    def is_within_appeal_period(self):
        today = timezone.now().date()
        return AppealConditions.objects.filter(start_date__lte=today, end_date__gte=today).exists()
    
    def application_check(self):
        student = Student.objects.get(user=self.request.user)
        today = timezone.now().date()
        return Application.objects.filter(student=student, created_at__year=today.year).exists()
    
    def has_already_appealed_this_year(self):
        try:
            student = Student.objects.get(user=self.request.user)
            current_year = timezone.now().year
            return Appeal.objects.filter(student=student, created_at__year=current_year).exists()
        except Student.DoesNotExist:
            return False
    
