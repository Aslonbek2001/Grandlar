from django.urls import path
from main.views import (
    view_about, view_home
    )

app_name = "main"

urlpatterns = [
    path('', view_home.index, name='index'),
    path('about/', view_about.about, name='about'),
]