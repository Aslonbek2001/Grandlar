from django.views.generic import ListView
from application.models import BallApplication

class ApplicationListView(ListView):
    model = BallApplication
    template_name = 'application/list.html'
    context_object_name = 'applications' 
    
    def get_queryset(self):
        user = self.request.user
        queryset = BallApplication.objects.all()
        training_filter = self.request.GET.get('training', None)
        spirituality_filter = self.request.GET.get('ball_spirituality', None)

        if user.role == 'student':
            return queryset.filter(application__student=user.profile)

        if user.role == 'training':
            if training_filter == 'exists':
                queryset = queryset.filter(ball_training__isnull=False)
            elif training_filter == 'none':
                queryset = queryset.filter(ball_training__isnull=True)
            
            return queryset
        
        elif user.role == 'spirituality':
            if spirituality_filter == 'exists':
                queryset = queryset.filter(ball_spirituality__isnull=False)
            elif spirituality_filter == 'none':
                queryset = queryset.filter(ball_spirituality__isnull=True)
            
            return queryset

        elif user.role == 'special':
            return queryset.filter(ball_spirituality__isnull=False,  ball_training__isnull=False)
        
        return BallApplication.objects.none()
    
        


        
        









