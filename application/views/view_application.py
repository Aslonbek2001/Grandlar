from django.shortcuts import render, redirect
from users.models import User
from django.views import View
from application.forms.create_application_hemis import ApplicationForm, UserForm
from django.contrib import messages
from application.models import Application, ApplicationStatus, BallApplication, YearlyApplicationWindow
from django.utils import timezone
from application.utils import get_course


class ApplicationCreateView(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            messages.info(request, "Hemis orqali kiring!")
            return redirect('main:index')
        
        try:
            profile = user.profile
        except User.profile.RelatedObjectDoesNotExist:
            messages.info(request, "Sizning ma'lumotlaringiz topilmadi!")
            return redirect('main:index')
        
        user_form = UserForm(instance=user)
        
        return render(request, 'application/create.html', {
            'user_form': user_form,
        })
        

    def post(self, request):
        form = ApplicationForm(request.POST, request.FILES)
        user = request.user
        student = user.profile
        date = timezone.now().date() 
        

        valid_window = YearlyApplicationWindow.objects.filter(year=date.year).first()
        if valid_window:
            if student.gpa < valid_window.min_gpa:
                messages.info(request, "Sizning GPA talablarga javob bermaydi.")
                return redirect('main:index') 
            

            if date < valid_window.start_date or date > valid_window.end_date:
                messages.info(request, "Ariza topshirish muddati tugagan.")
                return redirect('main:index')
            
            if not get_course(student.level, valid_window.course):
                messages.info(request, "Sizning kursingiz ushbu ariza oynasiga mos kelmaydi.")
                return redirect('main:index')
            
        if Application.objects.filter(student=student, created_at__year=date.year).exists():
            messages.info(request, "Siz bu yil ariza topshirgansiz allaqachon ariza topshirgansiz.")
            return redirect('main:index') 
        
        new_application = Application.objects.create(student=student, application_status=ApplicationStatus.NEW)
        ball_application = BallApplication.objects.create(application=new_application)
        messages.success(request, "Ariza muvofaqiyatli yuborildi")
        return redirect('main:index') 
    
