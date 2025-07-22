from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from application.models import BallApplication
from openpyxl import Workbook

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
    ws.append(['Full Name', 'Student ID Number', 'Passport Number', 
               'GPA', "Ta'lim",'Manaviyat'])

    ball_applications = BallApplication.objects.select_related(
        'application__student__user',
        'ball_training',
        'ball_spirituality'
    ).all()

    for ba in ball_applications:
        student = ba.application.student
        user = student.user

        # Har doim mavjud bo'lishiga ishonch yo‘q, shuning uchun null holatlarni tekshiramiz
        ball_training = ba.ball_training.field if ba.ball_training else ""
        ball_spirituality_total = ba.ball_spirituality.total if ba.ball_spirituality else ""

        ws.append([
            user.full_name,
            student.student_id_number,
            student.passport_number,
            student.gpa,
            ball_training,
            ball_spirituality_total
        ])

    # HTTP javobga yozish
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'
    wb.save(response)
    return response

