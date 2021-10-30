# importar el archivo de la conexión a la BD
from configdb import get_connection

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
        
        cursor.execute("SELECT id, date, id_user, price, balance from customer as us INNER JOIN invoice as I on I.id_user= us.id ORDER BY us.id ASC")

        if cursor.rowcount == 0 :

            cursor.execute("DELETE FROM customer WHERE id = %s",(id))
            cnn.commit()
            cnn.close() 

        else:
            print("El cliente todavia tiene facturas")

            #cnn.commit()
            cnn.close()    
    

def get_users():
    cnn = get_connection()
    customer = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer")
        customer = cursor.fetchall()
    cnn.close()

    print(cursor.rowcount)

    return customer

def get_user_id(id):
    cnn = get_connection()
    customer = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer WHERE id = %s",(id))
        customer = cursor.fetchone()
    cnn.close
    return customer


#----------------------------------------------------------------------------------------

def add_invoice(number,date,id_users, price, balance):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO invoice (number,date,id_users, price, balance) VALUES (%s,%s,%s,%s,%s)",(number,date,id_users, price, balance))
    cnn.commit()
    cnn.close()

def update_invoice(number,date,id_users, price, balance,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE invoice SET number = %s, date = %s, id_users = %s , price = %s , balance = %s WHERE id = %s",(number,date,id_users, price, balance))
    cnn.commit()
    cnn.close()

def delete_invoice(id):
    cnn = get_connection()
    with cnn.cursor() as cursor:

        cursor.execute("SELECT balance FROM invoice WHERE id = %s",(id))

        n = cursor.fetchall()

        if n == 0 :
            cursor.execute("DELETE FROM invoice WHERE id = %s",(id))
            cnn.commit()
            cnn.close() 

        else :
            print ("El total del balance no es cero")
            #cnn.commit()
            cnn.close()

def get_invoice():
    cnn = get_connection()
    invoice = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT number, date, id_users, price, balance FROM invoice")
        invoice = cursor.fetchall()
    cnn.close()

    print(invoice)

    return invoice

def get_invoice_id(id):
    cnn = get_connection()
    invoice = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, number, date, id_users, price, balance FROM invoice WHERE id = %s",(id))
        invoice = cursor.fetchone()
    cnn.close
    return invoice

def get_(id):
    cnn = get_connection()
    invoice = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, number, date, id_users, price, balance FROM invoice WHERE id = %s",(id))
        invoice = cursor.fetchone()
    cnn.close
    return invoice