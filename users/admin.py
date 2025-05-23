from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['full_name', 'role', 'created_at']
    list_filter = ['role']
    

admin.site.register(User, UserAdmin)

