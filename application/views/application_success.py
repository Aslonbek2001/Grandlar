from django.views.generic import TemplateView

class ApplicationSuccessView(TemplateView):
    template_name = 'application/success.html'
