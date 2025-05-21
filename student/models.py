from django.db import models
from users.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    student_id_number = models.CharField(verbose_name="Student ID", max_length=15)
    image = models.ImageField(verbose_name="Student rasmi", upload_to="downloads/")
    passport_number = models.CharField(verbose_name="Pasport raqami", max_length=10)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Student GPA')
    specialty = models.CharField(verbose_name="Mutaxasislik", max_length=100)
    studentStatus = models.CharField(verbose_name="Talaba xolati", max_length=20)
    educationForm = models.CharField(verbose_name="O'quv formati", max_length=50)
    group = models.CharField(verbose_name="Talaba gruh nomi", max_length=50)
    localityType = models.CharField(verbose_name="Hudud", max_length=50)
    level = models.CharField(verbose_name="Bosqich talabasi", max_length=50)
    semester = models.CharField(verbose_name="Semestr", max_length=50)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "student"
        ordering = ['-created_at']
        verbose_name = "Student"
        verbose_name_plural = "Students"
        indexes = [
            models.Index(fields=['student_id_number', 'passport_number']),
            models.Index(fields=['created_at']),  
        ]
    def __str__(self):
        return self.user.full_name