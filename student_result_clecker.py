from flask import Flask, render_template, request

app = Flask(__name__)

# Placeholder for student data (you can replace this with a database)
students = {
    "John": [85, 90, 78, 92, 88, 94],
    "Alice": [75, 86, 79, 65, 70, 80],
    "Bob": [92, 88, 87, 91, 85, 90],
}

# Function to calculate and return the result
def calculate_result(subject_marks):
    total = sum(subject_marks)
    num_distinctions = sum(mark >= 80 for mark in subject_marks)

    if all(mark >= 40 for mark in subject_marks):
        if num_distinctions == 6:
            return "Passed with 6 D"
        elif num_distinctions == 5:
            return "Passed with 5 D"
        elif num_distinctions == 4:
            return "Passed with 4 D"
        elif num_distinctions == 3:
            return "Passed with 3 D"
        elif num_distinctions == 2:
            return "Passed with 2 D"
        elif num_distinctions == 1:
            return "Passed with 1 D"
        else:
            return "Passed"
    else:
        return "Failed"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        student_name = request.form['student_name']
        if student_name in students:
            student_marks = students[student_name]
            result = calculate_result(student_marks)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
