from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from student.models import Student


"""Application Status - Ariza holati"""
class ApplicationStatus(models.TextChoices):
    NEW = 'new', 'Yangi'
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
    field1 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(20)], verbose_name="Kitobxonlik madaniyati (0-20)")
    field2 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(20)], verbose_name=""" "5 muxim tashabbus" doirasidagi to'garaklarda faol ishtiroki (0-20)""")
    field3 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(10)], verbose_name="Talabaning akademik o'zlashtirishi (0-10)")
    field4 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Talabaning oliy ta'lim tashkilotining ichki tartib qoidalari va odob-axloq kodeksiga rioya etishi (0-5)")
    field5 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(10)], verbose_name="Xalqaro, respublika, viloyat miqyosidagi ko'rik-tanlov, fan olimpiadalari va sport musobaqalarida erishgan natijalari (0-10)")
    field6 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Talabaning darslarga to'liq va kechikmasdan kelishi (0-5)")
    field7 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(10)], verbose_name=""" Talabalarning "Ma'rifat darslari" dagi faol ishtiroki (0-10)""")
    field8 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Volontyorlik va jamoat ishlaridagi faolligi (0-5)")
    field9 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Teatr va muzey, xiyobon, kino, tarixiy qadamjolarga tashriflar (0-5)")
    field10 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Talabalarning sport bilan shug‘ullanishi va sog‘lom turmush tarziga amal qilishi (0-5)")

    @property
    def total(self):
        fields = [f'field{i}' for i in range(1, 11)]
        return sum(getattr(self, field) or 0 for field in fields)
    
    @property
    def list_fields(self):
        fields = []
        for field_name in ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7', 'field8', 'field9', 'field10']:
            field_object = self._meta.get_field(field_name)
            verbose = field_object.verbose_name
            value = getattr(self, field_name)
            fields.append((verbose, value))
        return fields
    


class TrainingBall(models.Model):
    field = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, verbose_name="Talabaning o'zlshtirish ko'rsatkichi")


class BallApplication(models.Model):
    application = models.OneToOneField(to=Application, on_delete=models.CASCADE, related_name='apps')
    ball_spirituality = models.OneToOneField(to=SpiritualityBall, on_delete=models.CASCADE, related_name='spirituality', null=True, blank=True)
    ball_training = models.OneToOneField(to=TrainingBall, on_delete=models.CASCADE, related_name='training', null=True, blank=True)

    @property
    def total_ball(self):
        return self.ball_spirituality.total + self.ball_training.field



    def __str__(self):
        return f'{self.application.student.user.full_name}'





