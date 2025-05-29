from django.contrib import admin
from .models import Application, BallApplication, SpiritualityBall, TrainingBall, YearlyApplicationWindow


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'application_status', 'created_at']
    search_fields = ['user__username']
    list_filter = ['application_status']


class BallApplicationAdmin(admin.ModelAdmin):
    list_display = ['application', 'ball_spirituality', 'ball_training', 'total_ball']


class YearlyApplicationWindowAdmin(admin.ModelAdmin):
    #  Har bir yil uchun ariza topshirish shartlari o'chirilmasligi kerak. 
    #  Bu arizalarni yil bo'yicha filter qilish uchun kerak.
    list_display = ['year', 'min_gpa', 'start_date', 'end_date']
    search_fields = ['start_date', 'end_date']

admin.site.register(Application, ApplicationAdmin)
admin.site.register(BallApplication, BallApplicationAdmin)
admin.site.register(YearlyApplicationWindow, YearlyApplicationWindowAdmin)

admin.site.register(SpiritualityBall)
admin.site.register(TrainingBall)



