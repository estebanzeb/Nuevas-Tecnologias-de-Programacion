#Importar el archivo de la conexion de la base de datos 
from pymysql import connections
from configdb import get_connection 

def add_users(name, email, phone, password): 
    connections = get_connection()
    with connections.cursor() as cursor:
        cursor.execute("INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)", (name, email, phone, password))

    connections.commit()#Agregar
    connections.close()#Cerra la conexion

def update_users( name, email, phone, password, id):
    connections = get_connection
    with connections.cursor() as cursor:
        cursor.execute("UPDATE users name = %s, email = %s, phone = %s, password = %s WHERE id = %s ",( name, email, phone, password, id))     
    connections.commit()#Agregar
    connections.close()#Cerra la conexion
    
def delete_users(id):
    connections = get_connection()
    with connections.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s", (id))
    connections.commit()
    connections.close()

def get_users():
    connections = get_connection()
    users = []
    with connections.cursor() as cursor:
        cursor.execute("SELECT id, nombre, telefono FROM users")
        users = cursor.fetchall()
    connections.close()
    return users

def get_users_id(id):
    connections = get_connection()
    users = None
    with connections.cursor() as cursor:
        cursor.execute(
            "SELECT id, name, phone FROM users WHERE id = %s", (id))
        users = cursor.fetchone()
    connections.close()
    return users

