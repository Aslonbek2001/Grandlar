from student.models import Student
from application.models import Application, YearlyApplicationWindow
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
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
                raise Exception(f"Sizning GPA talablarga javob bermaydi. \n Minimal GPA: {valid_window.min_gpa}\n Sizning GPA: {student.gpa}\n Agar GPA ma'lumotlaringiz yangilanmagan bo'lsa, iltimos,Registrator offisiga murojaat qiling.")
            
            if date < valid_window.start_date or date > valid_window.end_date:
                raise Exception("Ariza topshirish yopiq.")
            
            if not get_course(student.level, valid_window.course):
                raise Exception("Sizning kursingiz bu yil ariza topshirish uchun mos emas.")
 
            
        if Application.objects.filter(student=student, created_at__year=date.year).exists():
            raise Exception("Siz allaqachon bu yil ariza topshirgansiz.")
      

class UserValidationService:
    def validate(self, request):
        user = request.user
        if not user.is_authenticated:
            raise Exception("Iltimos, Hemis orqali tizimga kiring.")

        try:
            return user.profile
        except ObjectDoesNotExist:
            raise Exception("Sizning talaba ma'lumotlaringiz topilmadi.")


class CombinedValidationService:
    def validate(self, request):
        user = request.user
        if not user.is_authenticated:
            raise Exception("Iltimos, Hemis orqali tizimga kiring.")

        try:
            student = user.profile
        except ObjectDoesNotExist:
            raise Exception("Sizning talaba ma'lumotlaringiz topilmadi.")

        date = timezone.now().date()
        valid_window = YearlyApplicationWindow.objects.filter(year=date.year).first()

        if valid_window:
            if student.gpa < valid_window.min_gpa:
                raise Exception(
                    f"Sizning GPA talablarga javob bermaydi. Minimal GPA: {valid_window.min_gpa}, Sizning GPA: {student.gpa}"
                )

            if not (valid_window.start_date <= date <= valid_window.end_date):
                raise Exception("Ariza topshirish muddati tugagan yoki boshlanmagan.")

            if not get_course(student.level, valid_window.course):
                raise Exception("Sizning kursingiz bu yil ariza topshirish uchun mos emas.")

        return student