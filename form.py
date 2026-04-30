from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ❌ Global connection (same as your old approach)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="negi123",
    database="students_data"
)

cursor = conn.cursor()

# 🏠 Form page
@app.route('/')
def student_form():
    return render_template("form.html")

# ➕ Add student
@app.route("/add", methods=['POST'])
def add_student():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="negi123",
        database="students_data"
    )
    cursor = conn.cursor()

    roll = request.form['roll']
    name = request.form['name']
    student_class = request.form['class']
    marks = request.form['marks']

    cursor.execute(
        "INSERT INTO students (roll_number, name, class, marks) VALUES (%s, %s, %s, %s)",
        (roll, name, student_class, marks)
    )
    conn.commit()
    

    return redirect(url_for('show_students'))

# 📄 Show data
@app.route('/students')
def show_students():
    conn = mysql.connector.connect(
       host="localhost",
        user="root",
        password="negi123",
        database="students_data"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    
    conn.close()

    print("DATA FROM DB:", data)

    return render_template("h.html", students=data)
# ▶️ Run
if __name__ == "__main__":
    app.run(debug=True)