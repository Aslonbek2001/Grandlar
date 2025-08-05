from django.urls import path
from appeal.views.appeal_create import AppealCreateView
from appeal.views.appeal_update import AppealUpdateView
from appeal.views.list import AppealListView
from appeal.views.answer_create import AnswerCreateView

from django.views.generic import TemplateView

app_name = 'appeal'

urlpatterns = [
    path('create/', AppealCreateView.as_view(), name='appeal_create'),
    # path('update/<int:pk>/', AppealUpdateView.as_view(), name='appeal_update'),
    path('list/', AppealListView.as_view(), name='appeal_list'),
    path('answer/create/<int:pk>/', AnswerCreateView.as_view(), name='answer_create'),

    


]