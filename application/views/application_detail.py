from django.views import View
from application.models import BallApplication
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
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

        if user.role == 'student' and ball.application.student != user.profile:
            messages.info(request, "Sizga ruxsat berilmagan!")
            return redirect('main:index')




        if user.role == 'training':
            form = TrainingBallForm(instance=ball.ball_training)
        elif user.role == 'spirituality':
            form = SpiritualityBallForm(instance=ball.ball_spirituality)
        elif user.role == 'special':
            app_obj = ball.application
            form = SpecialForm(instance=app_obj)
        else:
            return render(request, 'application/detail.html', {
            'application': ball
        })


        return render(request, 'application/detail.html', {
            'application': ball, 'form': form
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

        else:
            form = SpecialForm(request.POST)
            if form.is_valid():
                status = form.cleaned_data.get('application_status')
                application_obj = ball.application
                application_obj.application_status = status
                application_obj.save()
                messages.success(request, "Maxsus holat saqlandi.")
                return redirect('application:list')

        # Agar form xato bo'lsa yoki valid emas bo‘lsa
        return render(request, 'application/detail.html', {
            'application': ball,
            'form': form
        })
    

    

        


        
        









