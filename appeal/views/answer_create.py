from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from appeal.models import Appeal, AnswerToAppeal
from appeal.forms import AnswerForm
from django.contrib import messages
from django.shortcuts import redirect


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = AnswerToAppeal
    form_class = AnswerForm
    template_name = 'appeal/answer_create.html'
    success_url = reverse_lazy('appeal:appeal_list')

    def dispatch(self, request, *args, **kwargs):
        appeal_id = self.kwargs.get('pk')
        try:
            self.appeal = Appeal.objects.get(id=appeal_id)
        except Appeal.DoesNotExist:
            messages.error(request, "Apelatsiya topilmadi.")
            return redirect('appeal:appeal_list')

        if not self.is_expert():
            messages.error(request, "Siz ushbu apelatsiyaga javob berish huquqiga ega emassiz.")
            return redirect('appeal:appeal_list')

        return super().dispatch(request, *args, **kwargs)

    def is_expert(self):
        user = self.request.user
        return user.role in ['training', 'spirituality', 'special'] and not self.appeal.show_expert

    def form_valid(self, form):
        form.instance.appeal = self.appeal
        form.instance.expert = self.request.user
        messages.success(self.request, "Javob muvaffaqiyatli yuborildi.")
        return super().form_valid(form)


