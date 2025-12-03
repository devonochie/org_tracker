from db.connection import get_connection


def create_organization(name, country):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO organization(name, country) VALUES (%s, %s)", (name, country)) 
    conn.commit()

    conn.close()

def list_organization():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM organization")
    result = cursor.fetchall()

    conn.close()
    return result
