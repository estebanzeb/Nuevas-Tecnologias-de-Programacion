# importar el archivo de la conexión a la BD
from configdb import get_connection

def add_invoice(number,date,id_users, price, balance):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO customer (name, status, mobile) VALUES (%s,%s,%s)",(name,status,mobile))
    cnn.commit()
    cnn.close()

def add_user(name, status, mobile):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO customer (name, status, mobile) VALUES (%s,%s,%s)",(name,status,mobile))
    cnn.commit()
    cnn.close()

def update_user(name,status,mobile,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE customer SET name = %s, status = %s, mobile = %s WHERE id = %s",(name,status,mobile,id))
    cnn.commit()
    cnn.close()

def delete_user(id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM customer WHERE id = %s",(id))
    cnn.commit()
    cnn.close()

def get_users():
    cnn = get_connection()
    customer = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer")
        customer = cursor.fetchall()
    cnn.close()
    return customer

def get_user_id(id):
    cnn = get_connection()
    customer = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer WHERE id = %s",(id))
        customer = cursor.fetchone()
    cnn.close
    return customer
