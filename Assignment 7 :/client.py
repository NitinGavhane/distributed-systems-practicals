import requests

BASE_URL = 'http://localhost:5000'

def get_students():
    response = requests.get(f'{BASE_URL}/students')
    return response.json()

def get_student(student_id):
    response = requests.get(f'{BASE_URL}/students/{student_id}')
    return response.json()

#calling all the data from the student webservice
if __name__ == '__main__':
    students = get_students()
    print(students)

#Here we are calling the student data with specific "id" 
    student = get_student(1)
    print(student)
