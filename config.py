import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="KKK123@0",  # the password you just set
        database="company_db"
    )

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            dept_id INT AUTO_INCREMENT PRIMARY KEY,
            dept_name VARCHAR(255) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            job_id INT AUTO_INCREMENT PRIMARY KEY,
            job_title VARCHAR(255) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20),
            salary DECIMAL(10, 2),
            dept_id INT,
            job_id INT,
            FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
            FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        )
    """)
    