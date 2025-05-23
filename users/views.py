from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse

def custom_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')  # yoki superuser uchun boshqa URL
            else:
                return redirect(reverse('application:list'))
        else:
            return render(request, 'users/login.html', {'error': 'Username or password incorrect'})
    
    return render(request, 'users/login.html')
