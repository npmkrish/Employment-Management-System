from flask import Flask, render_template, request, redirect, url_for
from config import get_db_connection
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/employees')
def view_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT e.emp_id, e.first_name, e.last_name, e.email, e.phone, e.salary,
               d.dept_name, j.job_title
        FROM employees e
        LEFT JOIN departments d ON e.dept_id = d.dept_id
        LEFT JOIN jobs j ON e.job_id = j.job_id
    """)             
    employees = cursor.fetchall()
    conn.close()
    return render_template('view_employees.html', employees=employees)
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        salary = request.form['salary']
        dept_id = request.form['dept_id']
        job_id = request.form['job_id']
        cursor.execute("""
            INSERT INTO employees (first_name, last_name, email, phone, salary, dept_id, job_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, phone, salary, dept_id, job_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_employees'))

    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return render_template('add_employee.html', departments=departments, jobs=jobs)

@app.route('/delete/<int:emp_id>')
def delete_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_employees'))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
    app.run(port=5000)
