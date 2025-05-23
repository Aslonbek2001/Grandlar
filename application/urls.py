from django.urls import path
from application.views.view_application import ApplicationCreateView
from application.views.application_success import ApplicationSuccessView
from application.views.applications_list import ApplicationListView
from application.views.application_detail import ApplicationDetailView

app_name = 'application'

urlpatterns = [
    path('apply/', ApplicationCreateView.as_view(), name='create'),
    path('apply/success/', ApplicationSuccessView.as_view(), name='success'),
    path('list/', ApplicationListView.as_view(), name='list'),
    path("<int:pk>/", ApplicationDetailView.as_view(), name="detail"),
]
