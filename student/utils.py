from users.models import User
from student.models import Student
from django.core.files.base import ContentFile
import requests

def save_user_and_student(user_info: dict):
    data = user_info.get("data", {})
    
    # 1. User yaratish yoki yangilash
    user, created = User.objects.update_or_create(
        email=user_info["email"],
        defaults={
            "role": user_info.get("type", "student"),
            "full_name": data.get("full_name", ""),
            "phone": data.get("phone", ""),
            "address": data.get("address", ""),
        }
    )

    # 2. Rasmni yuklab olish
    image_url = data.get("image")
    image_file = None
    if image_url:
        try:
            img_response = requests.get(image_url)
            if img_response.status_code == 200:
                image_file = ContentFile(img_response.content, name=f"{user.username}_image.jpg")
        except Exception as e:
            print("Rasm yuklashda xatolik:", e)

    # 3. Student yaratish yoki yangilash
    student, created = Student.objects.update_or_create(
        user=user,
        defaults={
            "student_id_number": user_info.get("student_id_number"),
            "image": image_file if image_file else None,
            "passport_number": user_info.get("passport_number"),
            "gpa": 0.00,  # agar GPA yo'q bo'lsa default qiymat
            "specialty": data.get("specialty", {}).get("name", ""),
            "studentStatus": data.get("studentStatus", {}).get("name", ""),
            "educationForm": data.get("educationForm", {}).get("name", ""),
            "group": data.get("group", {}).get("name", ""),
            "localityType": data.get("faculty", {}).get("localityType", {}).get("name", ""),
            "level": data.get("level", {}).get("name", ""),
            "semester": data.get("semester", {}).get("name", ""),
        }
    )

    return user, student
