from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from application.models import BallApplication
from application.forms.ball_forms import SpiritualityBallForm, TrainingBallForm, SpecialForm

class ApplicationDetailView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        user = request.user
        ball = get_object_or_404(BallApplication, pk=pk)

        # Faqat student o'zining arizasini ko'rishi mumkin
        if user.role == 'student' and ball.application.student != user.profile:
            messages.info(request, "Sizga ruxsat berilmagan!")
            return redirect('main:index')

        form = None
        selected_status = None
        choices = None

        if user.role == 'training':
            if ball.ball_training:
                form = TrainingBallForm(instance=ball.ball_training)
            else:
                form = TrainingBallForm(initial={'field': ball.application.student.gpa * 16})

        elif user.role == 'spirituality':
            if ball.ball_spirituality:
                form = SpiritualityBallForm(instance=ball.ball_spirituality)
            else:
                form = SpiritualityBallForm(initial={'field3': ball.application.student.gpa * 2})

        elif user.role == 'special':
            app_obj = ball.application
            form = SpecialForm(instance=app_obj)
            selected_status = app_obj.application_status
            choices = form.fields['application_status'].choices

        return render(request, 'application/detail.html', {
            'application': ball,
            'form': form,
            'selected_status': selected_status,
            'choices': choices,
        })

    def post(self, request, pk):
        user = request.user
        ball = get_object_or_404(BallApplication, pk=pk)

        if user.role == 'training':
            form = TrainingBallForm(request.POST)
            if form.is_valid():
                training_instance = form.save()
                ball.ball_training = training_instance
                ball.save()
                messages.success(request, "Arizaga ball muvofaqiyatli qo'yildi!")
                return redirect('application:list')

        elif user.role == 'spirituality':
            form = SpiritualityBallForm(request.POST)
            if form.is_valid():
                spirituality_instance = form.save()
                ball.ball_spirituality = spirituality_instance
                ball.save()
                messages.success(request, "Arizaga ball muvofaqiyatli qo'yildi!")
                return redirect('application:list')

        if user.role == 'special':
            form = SpecialForm(request.POST, instance=ball.application)
            if form.is_valid():
                form.save()
                messages.success(request, "Maxsus holat saqlandi.")
                return redirect('application:list')
            else:
                selected_status = form.data.get('application_status')
                choices = form.fields['application_status'].choices
                return render(request, 'application/detail.html', {
                    'application': ball,
                    'form': form,
                    'selected_status': selected_status,
                    'choices': choices,
                })

        # Agar valid bo'lmasa
        return render(request, 'application/detail.html', {
            'application': ball,
            'form': form
        })




class ApplicationByUserView(View):
    def get(self, request, user_id):
        current_year = datetime.now().year
        try:
            # Arizani topamiz
            ball = BallApplication.objects.get(
                application__student__user__id=user_id,
                application__created_at__year=current_year
            )
            # Tayyor viewga redirect qilamiz
            return redirect(reverse('application:detail', kwargs={'pk': ball.pk}))
        except BallApplication.DoesNotExist:
            messages.error(request, "Ushbu foydalanuvchining joriy yil uchun arizasi topilmadi.")
            return redirect('main:index')