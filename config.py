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
    