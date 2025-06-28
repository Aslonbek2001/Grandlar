from student.models import Student
from application.models import Application, YearlyApplicationWindow
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from application.utils import get_course


class ApplicationValidationService:    
    def validate(self, request) -> Application:
        student = request.user.profile
        date = timezone.now().date() 
        valid_window = YearlyApplicationWindow.objects.filter(year=date.year).first()
        if valid_window:
            if student.gpa < valid_window.min_gpa:
                messages.info(request, f"Sizning GPA talablarga javob bermaydi. \n Minimal GPA: {valid_window.min_gpa}\n Sizning GPA: {student.gpa}\n Agar GPA ma'lumotlaringiz yangilanmagan bo'lsa, iltimos,Registrator offisiga murojaat qiling.")
                return redirect('main:index') 
            
            if date < valid_window.start_date or date > valid_window.end_date:
                messages.info(request, "Ariza topshirish yopiq.")
                return redirect('main:index')
            
            if not get_course(student.level, valid_window.course):
                messages.info(request, "Sizning kursingiz bu yil ariza topshirish uchun mos emas.")
                return redirect('main:index')
            
        if Application.objects.filter(student=student, created_at__year=date.year).exists():
            messages.info(request, "Siz allaqachon bu yil ariza topshirgansiz.")
            return redirect('main:index') 
        

class UserValidationService:
    def validate(self, request):
        user = request.user
        if not user.is_authenticated:
            messages.info(request, "Hemis orqali kiring!")
            return redirect('main:index')
        
        try:
            student = user.profile
            return student
        except Student.DoesNotExist:
            messages.info(request, "Sizning ma'lumotlaringiz topilmadi!")
            return redirect('main:index')
        