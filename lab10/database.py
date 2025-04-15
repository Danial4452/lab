import psycopg2
from psycopg2 import sql

# Подключение к базе данных PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        dbname="snake_db",  # Название базы данных
        user="postgres",  # Имя пользователя
        password="your_password",  # Пароль
        host="localhost",  # Обычно localhost
        port="5432"  # Обычно 5432
    )

# Функция для создания таблиц (если их нет)
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "user" (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        user_id INT REFERENCES "user"(id) ON DELETE CASCADE,
        score INT DEFAULT 0,
        level INT DEFAULT 1,
        PRIMARY KEY (user_id)
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()

# Функция для получения или создания пользователя
def get_or_create_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM \"user\" WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        user_id = user[0]
        cursor.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        if row:
            score, level = row
        else:
            cursor.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
            conn.commit()
            score, level = 0, 1
    else:
        cursor.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING id", (username,))
        user_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        score, level = 0, 1

    cursor.close()
    conn.close()
    return user_id, score, level

# Функция для сохранения прогресса
def save_progress(user_id, score, level):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE user_score 
    SET score = %s, level = %s 
    WHERE user_id = %s
    """, (score, level, user_id))

    conn.commit()
    cursor.close()
    conn.close()