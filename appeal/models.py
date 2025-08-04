from django.db import models
from student.models import Student
from django.conf import settings

# Create your models here.

class AppealConditions(models.Model):
    start_date = models.DateField(verbose_name="Boshlanish sanasi")
    end_date = models.DateField(verbose_name="Tugash sanasi")
    year = models.IntegerField(verbose_name="Yil")

    def __str__(self):
        return f"{self.year} yil uchun apelatsiya shartlari"    

class Appeal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='appeals')
    message = models.TextField(null=True, blank=True)
    message_file = models.FileField(upload_to='appeals/', blank=True, null=True)
    show_expert = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appeal from {self.student} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class AnswerToAppeal(models.Model):
    appeal = models.OneToOneField(Appeal, on_delete=models.CASCADE, related_name='answer')
    expert = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expert_answers')
    answer_text = models.TextField()
    show_student = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Answer to {self.appeal} by {self.expert.username} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

