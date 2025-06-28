from student.models import Student
from application.models import BallApplication
from application.models import Application, ApplicationStatus, BallApplication
from application.services.validation import ApplicationValidationService


class ApplicationCreationService:
    validation_application = ApplicationValidationService()

    def create(self, request, form) -> Application:
        self.validation_application.validate(request)
        student = request.user.profile
        application = form.save(commit=False)
        application.student = student
        application.academic_performance = student.gpa * 2
        application.application_status = ApplicationStatus.NEW
        application.save()
        BallApplication.objects.create(application=application)
        return application
    