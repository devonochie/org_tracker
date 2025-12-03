from db.connection import get_connection


def create_department(organization_id, name):
    conn = get_connection()
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO department (organization_id, name) VALUES (%s, %s)", (organization_id, name))
    conn.commit()
    conn.close()
    
def list_department_by_organization(organization_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM department WHERE organization_id = %s", (organization_id,))
    result = cursor.fetchall()
    conn.close()
    return result

def list_department():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute()
    cursor.execute("SELECT * FROM department")
    result = cursor.fetchall()
    conn.close()
    return result
