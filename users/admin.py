from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

# User yaratish uchun form
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Parol', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Parolni tasdiqlash', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'role', 'phone', 'address')

    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Parollar mos kelmadi")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Parolni hash qiladi
        if commit:
            user.save()
        return user

# User o'zgartirish uchun form
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Parol",
        help_text=("Parolni o'zgartirish uchun <a href=\"../password/\">bu yerga</a> bosing."))

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'role', 'phone', 'address', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('full_name', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')

    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')}),
        ("Qo'shimcha ma'lumotlar", {'fields': ('role', 'phone', 'address')}),
        ('Ruxsatlar', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'role', 'phone', 'address', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )

    search_fields = ('full_name', 'email')
    ordering = ('full_name',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)
