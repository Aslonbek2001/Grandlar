from django.urls import path
from main.views import (
    view_home, logout
    )

app_name = "main"

urlpatterns = [
    path('', view_home.index, name='index'),
    path('logout/', logout.logout_view, name='logout'),
]