from django.contrib import admin
from .models import Appeal, AppealConditions, AnswerToAppeal

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('student', 'message', 'created_at', 'updated_at')
    search_fields = ('student__user__username', 'message')
    list_filter = ('show_expert', 'created_at')
    ordering = ('-created_at',)


@admin.register(AppealConditions)
class AppealConditionsAdmin(admin.ModelAdmin):
    list_display = ('year', 'start_date', 'end_date')
    search_fields = ('year',)
    ordering = ('-year',)

@admin.register(AnswerToAppeal)
class AnswerToAppealAdmin(admin.ModelAdmin):
    list_display = ('appeal', 'expert', 'created_at', 'show_student')
    search_fields = ('appeal__student__user__username', 'expert__username')
    list_filter = ('show_student', 'created_at')
    ordering = ('-created_at',)
