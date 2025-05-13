from django.db import models


"""Privilege Category - Imtiyozlar toifasi"""
class PrivilegeCategory(models.TextChoices):
    UNDEFINED = 'undefined', 'Undefined'
    STUDENT = 'student', 'Student'
    EMPLOYEE = 'employee', 'Employee'
    ADMIN = 'admin', 'Admin'

"""Education Direction - Ta'lim yo'nalishi"""
class EducationDirection(models.TextChoices):
    UNDEFINED = 'undefined', 'Undefined'
    SCIENCE = 'science', 'Science'
    ENGINEERING = 'engineering', 'Engineering'
    ARTS = 'arts', 'Arts'
    BUSINESS = 'business', 'Business'
    MEDICINE = 'medicine', 'Medicine'


"""Education Level - Ta'lim darajasi"""
class EducationLevel(models.TextChoices):
    UNDEFINED = 'undefined', 'Undefined'
    HIGH_SCHOOL = 'high_school', 'High School'
    BACHELORS = 'bachelors', 'Bachelors'
    MASTERS = 'masters', 'Masters'
    DOCTORATE = 'doctorate', 'Doctorate'


"""Application Status - Ariza holati"""
class ApplicationStatus(models.TextChoices):
    NEW = 'new', 'New'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'



"""Application model - Ariza modeli"""
class Application(models.Model):
    student_id = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='Student ID')
    student_name = models.CharField(max_length=100, verbose_name='Student Name')
    student_phone = models.CharField(max_length=15, verbose_name='Student Phone')
    student_address = models.TextField(verbose_name='Student Address')
    student_gpa = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Student GPA')
    student_education_direction = models.CharField(
        max_length=20,
        choices=EducationDirection.choices,
        default=EducationDirection.UNDEFINED,
        verbose_name="Ta'lim yo'nalishi"
    )
    student_privilege_category = models.CharField(
        max_length=20,
        choices=PrivilegeCategory.choices,
        default=PrivilegeCategory.UNDEFINED,
        verbose_name="Imtiyozlar toifasi"
    )
    student_education_level = models.CharField(
        max_length=20,
        choices=EducationLevel.choices,
        default=EducationLevel.UNDEFINED,
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
        return f" {self.student_name} - {self.application_status}"
    
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
            models.Index(fields=['student_name']),
            models.Index(fields=['student_phone']),
            models.Index(fields=['student_education_direction']),
            models.Index(fields=['student_privilege_category']),
            models.Index(fields=['student_education_level']),
            models.Index(fields=['application_status']),
            models.Index(fields=['created_at']),
        ]

