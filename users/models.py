# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# accounts/models.py
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, email=None, password=None, **extra_fields):
        if not full_name:
            raise ValueError('Foydalanuvchi nomi (full_name) majburiy')
        email = self.normalize_email(email)
        user = self.model(full_name=full_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bo‘lishi kerak.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is_superuser=True bo‘lishi kerak.')

        return self.create_user(full_name, email, password, **extra_fields)


class User(AbstractUser):
    username = None
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('training', "Training"),
        ('spirituality', 'Spirituality'),
        ('special', 'Special')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    full_name = models.CharField(verbose_name="To'liq ism sharifi", unique=True, max_length=100)
    phone = models.CharField(verbose_name="Telefon raqami", max_length=20)
    address = models.CharField(verbose_name="Yashash manzili", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name
