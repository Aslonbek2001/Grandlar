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
    
    academic_performance = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True, blank=True,
        verbose_name="Akademik o'zlashtirish ko'rsatkichi (GPA*2)",
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(100.00)
        ]
    )
    reading_culture = models.FileField(
        upload_to='uploads/', 
        verbose_name="Kitobxonlik madaniyati", 
        null=True, blank=True)
    
    five_initiatives = models.FileField(
        upload_to='uploads/',
        verbose_name='"5 muhim tashabbus" doirasidagi to\'garaklarda faol ishtiroki',
        null=True, blank=True)
    
    manners = models.FileField(
        upload_to='uploads/',
        verbose_name="Talabaning oliy ta'lim tashkilotining ichki tartib qoidalari va Odob-axloq kodeksiga rioya etishi (0-5)",
        null=True, blank=True)
    
    participation_in_events = models.FileField(
        upload_to='uploads/',
        verbose_name="Xalqaro, respublika, viloyat miqyosidagi ko'rik-tanlov, fan olimpiadalari va sport musobaqalarida erishgan natijalari",
        null=True, blank=True)
    
    attendance = models.FileField(
        upload_to='uploads/',
        verbose_name="Talabaning darslarga to'liq va kechikmasdan kelishi (0-5)",
        null=True, blank=True)
    
    enlightenment_classes = models.FileField(
        upload_to='uploads/',
        verbose_name='Talabaning "Ma\'rifat darslari"dagi faol ishtiroki',
        null=True, blank=True)
    
    volunteer_work = models.FileField(
        upload_to='uploads/',
        verbose_name="Volontyorlik va jamoat ishlaridagi faolligi",
        null=True, blank=True)
    
    cultural_visits = models.FileField(
        upload_to='uploads/',
        verbose_name="Teatr va muzey, xiyobon, kino, tarixiy qadamjolarga tashriflar",
        null=True, blank=True)
    
    sports_activity = models.FileField(
        upload_to='uploads/',
        verbose_name="Talabalarning sport bilan shug‘ullanishi va sog‘lom turmush tarziga amal qilishi",
        null=True, blank=True)
    
    spiritual_enlightenment = models.FileField(
        upload_to='uploads/',
        verbose_name="Ma'naviy-ma'rifiy sohaga oid boshqa yo'nalishlardagi faoliyati",
        null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.full_name}"
    
    def approve(self):
        self.application_status = ApplicationStatus.APPROVED
        self.save()

    def reject(self):
        self.application_status = ApplicationStatus.REJECTED
        self.save()

    
    
    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['application_status']),
            models.Index(fields=['created_at']),
        ]


class SpiritualityBall(models.Model):
    field1 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(20)], verbose_name="Kitobxonlik madaniyati (0-20)")
    field2 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(20)], verbose_name=""" "5 muxim tashabbus" doirasidagi to'garaklarda faol ishtiroki (0-20)""")
    field3 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(10)], verbose_name="Talabaning akademik o'zlashtirishi (0-10)")
    field4 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Talabaning oliy ta'lim tashkilotining ichki tartib qoidalari va odob-axloq kodeksiga rioya etishi (0-5)")
    field5 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(10)], verbose_name="Xalqaro, respublika, viloyat miqyosidagi ko'rik-tanlov, fan olimpiadalari va sport musobaqalarida erishgan natijalari (0-10)")
    field6 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Talabaning darslarga to'liq va kechikmasdan kelishi (0-5)")
    field7 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(10)], verbose_name=""" Talabalarning "Ma'rifat darslari" dagi faol ishtiroki (0-10)""")
    field8 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Volontyorlik va jamoat ishlaridagi faolligi (0-5)")
    field9 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Teatr va muzey, xiyobon, kino, tarixiy qadamjolarga tashriflar (0-5)")
    field10 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Talabalarning sport bilan shug‘ullanishi va sog‘lom turmush tarziga amal qilishi (0-5)")
    field11 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, validators=[ MinValueValidator(0), MaxValueValidator(5)], verbose_name="Manaviy-ma'rifiy sohaga oid boshqa yo'nalishlardagi faoligi (0-5)")


    @property
    def total(self):
        return sum([self.field1, self.field2, self.field3, self.field4, self.field5, 
                    self.field6, self.field7, self.field8, self.field9, self.field10, self.field11]) / 5
    

    @property
    def list_fields(self):
        fields = []
        for field_name in ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7', 'field8', 'field9', 'field10', 'field11']:
            field_object = self._meta.get_field(field_name)
            verbose = field_object.verbose_name
            value = getattr(self, field_name)
            fields.append((verbose, value))
        return fields
    
    def __str__(self):
        return str(self.total)
    
    class Meta:
        verbose_name = "Ijtimoiy faollik qo'ygan bal"
        verbose_name_plural = "Ijtimoiy faollik qo'ygan ballar"


class TrainingBall(models.Model):
    field = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, verbose_name="Talabaning o'zlshtirish ko'rsatkichi")

    def __str__(self):
        return str(self.field)
    
    class Meta:
        verbose_name = "Akademik o'zlashtirish bo'yicha ball"
        verbose_name_plural = "Akademik o'zlashtirish bo'yicha ballar"

class BallApplication(models.Model):
    application = models.OneToOneField(to=Application, on_delete=models.CASCADE, related_name='apps')
    ball_spirituality = models.OneToOneField(to=SpiritualityBall, on_delete=models.CASCADE, related_name='spirituality', null=True, blank=True)
    ball_training = models.OneToOneField(to=TrainingBall, on_delete=models.CASCADE, related_name='training', null=True, blank=True)

    @property
    def total_ball(self):
        spirituality_score = self.ball_spirituality.total if self.ball_spirituality else 0
        training_score = self.ball_training.field if self.ball_training else 0
        return (spirituality_score + training_score)

    def __str__(self):
        return f'{self.application.student.user.full_name}'

    class Meta:
        verbose_name = "Ariza bo'yicha ball"
        verbose_name_plural = "Arizalar bo'yicha ballar"
  


class YearlyApplicationWindow(models.Model):
    year = models.IntegerField()
    course = models.IntegerField(help_text="Nechanchi kurslar uchun ochilgan (1, 2, ...)")
    min_gpa = models.DecimalField(
        max_digits=3, decimal_places=1, default=3.5,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Talabaning minimal GPA balli (0.0 - 5.0)",
        verbose_name="Minimal GPA"
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.year} yil uchun {self.course}-kurs ariza oynasi"
    
    class Meta:
        verbose_name = "Ariza topshirish uchun shart"
        verbose_name_plural = "Ariza topshirish uchun shartlar"

