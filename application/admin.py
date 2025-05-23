import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import Application, BallApplication, SpiritualityBall, TrainingBall

# class ApplicationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'student_id', 'student_name', 'student_gpa', 'student_education_direction', 'student_privilege_category', 'student_education_level', 'application_status', 'created_at')
#     search_fields = ('student_id', 'student_name', 'student_phone', 'student_education_direction', 'student_privilege_category', 'student_education_level')
#     list_filter = ('student_education_direction', 'student_privilege_category', 'student_education_level')
#     ordering = ('-id',)
#     list_display_links = ('student_id', 'student_name')
#     actions = ['export_as_excel']

#     def export_as_excel(self, request, queryset):
#         # Excel workbook va sheet yaratish
#         wb = openpyxl.Workbook()
#         ws = wb.active
#         ws.title = "Applications"

#         # Sarlavhalar
#         headers = [
#             'ID', 'Student ID', 'Name', 'Phone', 'Address', 'GPA',
#             "Direction", "Privilege", "Level", "Status", "Created At", "Updated At"
#         ]
#         ws.append(headers)

#         # Ma'lumotlar
#         for obj in queryset:
#             ws.append([
#                 obj.id,
#                 obj.student_id,
#                 obj.student_name,
#                 obj.student_phone,
#                 obj.student_address,
#                 float(obj.student_gpa),
#                 obj.student_education_direction,
#                 obj.student_privilege_category,
#                 obj.student_education_level,
#                 obj.application_status,
#                 obj.created_at.strftime('%Y-%m-%d %H:%M'),
#                 obj.updated_at.strftime('%Y-%m-%d %H:%M'),
#             ])

#         # Javob yuborish
#         response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#         response['Content-Disposition'] = 'attachment; filename=applications.xlsx'
#         wb.save(response)
#         return response

#     export_as_excel.short_description = "Export selected to Excel"

# admin.site.register(Application, ApplicationAdmin)

admin.site.register(Application)
admin.site.register(BallApplication)
admin.site.register(TrainingBall)
admin.site.register(SpiritualityBall)

