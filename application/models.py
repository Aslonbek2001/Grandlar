from django.db import models
from student.models import Student

"""Application Status - Ariza holati"""
class ApplicationStatus(models.TextChoices):
    NEW = 'new', 'New'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'

"""Application model - Ariza modeli"""
class Application(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="applications" )
    student_education_direction = models.CharField(
        max_length=20,
        verbose_name="Ta'lim yo'nalishi"
    )
    student_privilege_category = models.CharField(
        max_length=20,
        verbose_name="Imtiyozlar toifasi"
    )
    student_education_level = models.CharField(
        max_length=20,
        verbose_name="Ta'lim darajasi"
    )

    application_status = models.CharField(
        max_length=10,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.NEW,
        verbose_name="Ariza holati"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.application_status}"
    
    def approve(self):
        self.application_status != ApplicationStatus.APPROVED
        self.application_status = ApplicationStatus.APPROVED
        self.save()

    def reject(self):
        self.application_status != ApplicationStatus.REJECTED
        self.application_status = ApplicationStatus.REJECTED
        self.save()
    
    
    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ['-created_at']
        indexes = [
            
      
            models.Index(fields=['student_education_direction']),
            models.Index(fields=['student_privilege_category']),
            models.Index(fields=['student_education_level']),
            models.Index(fields=['application_status']),
            models.Index(fields=['created_at']),
        ]

