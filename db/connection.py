import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            password=os.getenv("DB_PASSWORD"),
            user= os.getenv("DB_USER"),
            database= os.getenv("DB_DATABASE")
        )
        if conn.is_connected():
            print("Connected to MySQL")
            return conn
    except Error as e:
        raise RuntimeError(f"Failed to connect to database: {e}")
