from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def logout_view(request):
    logout(request)

    messages.success(request, 'Siz profilingizdan muvaffaqiyatli chiqdingiz.')

    return redirect('main:index')  # foydalanuvchini login sahifasiga yo‘naltiradi
