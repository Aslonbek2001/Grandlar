import json 
import logging
import requests


HEMIS_TOKEN = "U8oL71AD92zVfKfCq0jjnPKU3MKqSXb6"


def get_user_info_by_student_id(student_id: int):
    api_url = 'https://student.uzgeouniver.uz/rest/v1/data/student-list'

    headers = {
        'Authorization': f'Bearer {HEMIS_TOKEN}'
    }
    try:
        response = requests.get(api_url, headers=headers)
    except:
        logging.info("Xatolik", response.status_code, response.text)
 



get_user_info_by_student_id(403241100600)