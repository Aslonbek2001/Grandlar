from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse

def custom_login_view(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        password = request.POST['password']
        print(f"Attempting login for user: {full_name}")
        print(f"Password provided: {password}")


        user = authenticate(request, username=full_name, password=password)

        print(f"Authentication result: {user}")

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect(reverse('application:list'))
        else:
            return render(request, 'users/login.html', {'error': 'F.I.Sh yoki parol noto‘g‘ri'})
    
    return render(request, 'users/login.html')

