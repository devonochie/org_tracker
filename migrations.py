from db.connection import get_connection


def run_migrations():
    conn = get_connection()
    cursor = conn.cursor()
    if not conn:
        print("No database connection")
        return
    #--- Organization Table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS organization(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            country VARCHAR(255) NOT NULL, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    #--- department Table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS department(
            id INT AUTO_INCREMENT PRIMARY KEY,
            organization_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(organization_id) REFERENCES organization(id) ON DELETE CASCADE
        )
    """)    
    # --- users table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            department_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (department_id) REFERENCES department(id) ON DELETE CASCADE
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Migrations executed successfully!")
