import mysql.connector

try:
    print("🔍 Trying to connect to MySQL...")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="KKK123@0",   # your password here, if any
        database="company_db",
        connection_timeout=5
        
    )
    if conn.is_connected():
        print("✅ Database connection successful!")
    conn.close()
except mysql.connector.Error as e:
    print("❌ Database connection failed:", e)
except Exception as ex:
    print("⚠️ Unexpected error:", ex)
