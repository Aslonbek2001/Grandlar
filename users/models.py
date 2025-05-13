# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.Choices):
    STUDENT = 'student', 'Student'
    EMPLOYEE = 'employee', 'Employee'

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    first_name = models.CharField(verbose_name="Ism", max_length=50)
    second_name = models.CharField(verbose_name="Familiya", max_length=50)
    third_name = models.CharField(verbose_name="Otasining ismi", max_length=50)
    full_name = models.CharField(verbose_name="To'liq ism sharifi", max_length=50)
    short_name = models.CharField(verbose_name="Qisqa ism", max_length=50)
    phone = models.CharField(verbose_name="Telefon raqami", max_length=20)
    address = models.CharField(verbose_name="Yashash manzili", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.full_name
