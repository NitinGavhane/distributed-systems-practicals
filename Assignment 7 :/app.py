from flask import Flask, jsonify

app = Flask(__name__)

# Sample data representing student information 
students = [
    {
        'id': 1,
        'name': 'Tony Stark',
        'age': 23,
        'major': 'Robotics Technology'
    },
    {
        'id': 2,
        'name': 'Himanshu Wankar',
        'age': 24,
        'major': 'Information Technology'
    },
    {
        'id': 3,
        'name': 'Thor OdinSon',
        'age': 30,
        'major': 'Electrical Engineering'
    },
    {
        'id': 4,
        'name': 'Natasha Romanoff',
        'age': 20,
        'major': 'Psychology'
    },
    {
        'id': 5,
        'name': 'Bruce Bannner',
        'age': 22,
        'major': 'Partical Physics'
    },
    {
        'id': 6,
        'name': 'Hank Pim',
        'age': 35,
        'major': 'Quantam Physics'
    }
]

@app.route('/students')
def get_students():
    return jsonify(students)

@app.route('/students/<int:student_id>')
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run()

