from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from appeal.models import Appeal, AnswerToAppeal
from appeal.forms import AnswerForm
from django.contrib import messages
from django.shortcuts import redirect


class AnswerUpdateView(LoginRequiredMixin, UpdateView):
    model = AnswerToAppeal
    form_class = AnswerForm
    template_name = 'appeal/answer_update.html'
    success_url = reverse_lazy('appeal:appeal_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.appeal = self.object.appeal

        # 1️⃣ Faqat javobni yozgan ekspert yoki tegishli rol egalari tahrir qila oladi
        if not self.can_edit():
            messages.error(request, "Siz ushbu javobni tahrirlash huquqiga ega emassiz.")
            return redirect('appeal:appeal_list')

        return super().dispatch(request, *args, **kwargs)

    def can_edit(self):
        user = self.request.user
        # Javob muallifi bo‘lishi yoki ruxsatli ekspert roli bo‘lishi kerak
        return (
            self.object.expert == user or
            (user.role in ['training', 'spirituality', 'special'])
        )

    def form_valid(self, form):
        messages.success(self.request, "Javob muvaffaqiyatli yangilandi.")
        return super().form_valid(form)
