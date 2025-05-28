
def get_course(student_level: str, course: int) -> bool:
    import re
    match = re.search(r'\d+', student_level)
    if not match:
        return False
    
    student_course_number = match.group() 
    

    return student_course_number in str(course)