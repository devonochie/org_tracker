from db.connection import get_connection

def create_employee(department_id, name, email):
    conn = get_connection()
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO users (department_id, name, email) VALUES (%s, %s)", (department_id, name, email))
    conn.commit()
    conn.close()