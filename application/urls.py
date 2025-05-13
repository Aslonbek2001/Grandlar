from django.urls import path
from application.views.view_application import ApplicationCreateView
from application.views.application_success import ApplicationSuccessView

app_name = 'application'

urlpatterns = [
    path('apply/', ApplicationCreateView.as_view(), name='create'),
    path('apply/success/', ApplicationSuccessView.as_view(), name='success'),

]

