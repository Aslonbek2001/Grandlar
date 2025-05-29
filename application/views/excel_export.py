from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from openpyxl import Workbook
from application.models import Application

def export_students_excel(request):

    user = request.user

    if user.role != 'special':
        messages.info(request, "Sizga bunday ruxsat berilmagan!")
        return redirect('application:list')
    
    print("user:", user.role)
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Talabalar"

    # Ustunlar
    ws.append(['Full Name', 'Student ID Number', 'Passport Number', 'GPA', 'Application Status'])

    applications = Application.objects.select_related('student__user').all()

    for app in applications:
        student = app.student
        user = student.user
        ws.append([
            user.full_name,
            student.student_id_number,
            student.passport_number,
            float(student.gpa),
            app.application_status
        ])

    # HTTP javobga yozish
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'
    wb.save(response)
    return response

