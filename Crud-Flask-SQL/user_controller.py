# importar el archivo de la conexión a la BD
from configdb import get_connection

def add_user(name,email,phone,password):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO users (name, email, phone, password) VALUES (%s,%s,%s,%s)",(name,email,phone,password))
    cnn.commit()
    cnn.close()

def update_user(name,email,phone,password,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE users SET name = %s, email = %s, phone = %s, password = %s WHERE id = %s",(name,email,phone,password,id))
    cnn.commit()
    cnn.close()

def delete_user(id):
    cnn = get_connection()

    


    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s",(id))
    cnn.commit()
    cnn.close()

def get_users():
    cnn = get_connection()
    users = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, phone FROM users")
        users = cursor.fetchall()
    cnn.close()
    return users

def get_user_id(id):
    cnn = get_connection()
    user = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, phone FROM users WHERE id = %s",(id))
        user = cursor.fetchone()
    cnn.close
    return user
