import psycopg2
from db import get_db_connection

def create_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS auth (
            id SERIAL PRIMARY KEY,
            user_id INT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Tablas creadas correctamente.")

if __name__ == "__main__":
    create_tables()

