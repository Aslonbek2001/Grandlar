from django.db import models
from student.models import Student


"""Application Status - Ariza holati"""
class ApplicationStatus(models.TextChoices):
    NEW = 'new', 'New'
    APPROVED = 'approved', 'Tasdiqlandi'
    REJECTED = 'rejected', 'Rad etildi'

"""Application model - Ariza modeli"""


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="applications")
    application_status = models.CharField(
        max_length=10,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.NEW,
        verbose_name="Ariza holati"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.full_name} - {self.application_status}"
    
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
            models.Index(fields=['application_status']),
            models.Index(fields=['created_at']),
        ]


class SpiritualityBall(models.Model):
    field1 = models.DecimalField(max_digits=3, decimal_places=1,)
    field2 = models.DecimalField(max_digits=3, decimal_places=1)
    field3 = models.DecimalField(max_digits=3, decimal_places=1)
    field4 = models.DecimalField(max_digits=3, decimal_places=1)
    field5 = models.DecimalField(max_digits=3, decimal_places=1)
    field6 = models.DecimalField(max_digits=3, decimal_places=1)
    field7 = models.DecimalField(max_digits=3, decimal_places=1)
    field8 = models.DecimalField(max_digits=3, decimal_places=1)
    field9 = models.DecimalField(max_digits=3, decimal_places=1)
    field10 = models.DecimalField(max_digits=3, decimal_places=1)

    @property
    def total(self):
        return (
            self.field1 + self.field2 + self.field3 + self.field4 + self.field5 +
            self.field6 + self.field7 + self.field8 + self.field9 + self.field10
        )
    


class TrainingBall(models.Model):
    field = models.DecimalField(max_digits=3, decimal_places=1)


class BallApplication(models.Model):
    application = models.OneToOneField(to=Application, on_delete=models.CASCADE, related_name='apps')
    ball_spirituality = models.OneToOneField(to=SpiritualityBall, on_delete=models.CASCADE, related_name='spirituality', null=True, blank=True)
    ball_training = models.OneToOneField(to=TrainingBall, on_delete=models.CASCADE, related_name='training', null=True, blank=True)

    def __str__(self):
        return f'{self.application.student.user.full_name}'





