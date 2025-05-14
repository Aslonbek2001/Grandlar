from django.shortcuts import render
from django.views import View


def profile_view(request):
    return render(request, 'result/profile.html')