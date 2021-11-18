# importar el archivo de la conexión a la BD
from configdb import get_connection

def get_count_users():
    cnn = get_connection()
    count = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM dbbiblioteca.user ")
        count = cursor.fetchone()
    cnn.close()
    return count

def get_login():
    cnn = get_connection()
    user = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT  id,name, email, password FROM user")
        user = cursor.fetchall()
    cnn.close()
    return user

#----------------------------------------------------------------------------------------

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
    usercount = get_user_id2(id)

    if(usercount[1] == 0):
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

def get_user_id2(id):
    cnn = get_connection()
    customer2 = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT US.id,(select count(*) from dbbiblioteca.invoice where id_user=US.id) invoices FROM dbbiblioteca.customer AS US WHERE US.id=%s",(id))
        customer2 = cursor.fetchone()
    cnn.close
    return customer2
#----------------------------------------------------------------------------------------

def add_invoice(number,date,id_user, price, balance):
    cnn = get_connection()
    invoicecount = get_invoice_id2(id_user)
    #print(invoicecount)
    if(invoicecount != None):
        with cnn.cursor() as cursor:
            cursor.execute("INSERT INTO invoice (number, date, id_user, price, balance) VALUES (%s,%s,%s,%s,%s)",(number, date, id_user, price, balance))
        cnn.commit()
        cnn.close()   
        
def update_invoice(number, date, price,balance,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE invoice SET number = %s, date = %s, price = %s , balance = %s WHERE id = %s",(number, date, price,balance,id))
    cnn.commit()
    cnn.close()

def delete_invoice(id):
    cnn = get_connection()
    balance = get_invoice_id(id)[5]
    print (balance)
    var_dump = balance
    if (balance == "0"):
        with cnn.cursor() as cursor:
            cursor.execute("DELETE FROM invoice WHERE id = %s",(id))
        cnn.commit()
        cnn.close()

def get_invoice():
    cnn = get_connection()
    invoice = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT I.id, I.number, I.date, US.id, price, balance   FROM customer AS US INNER JOIN invoice AS I ON I.id_user= US.id ORDER BY US.id ASC")
        invoice = cursor.fetchall()
    cnn.close()
    print(invoice)
    return invoice

def get_invoice_id(id):
    cnn = get_connection()
    invoice = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT I.id, I.number, I.date, US.id, price, balance  FROM customer AS US INNER JOIN invoice AS I ON I.id_user= US.id WHERE I.id = %s",(id))
        invoice = cursor.fetchone()
    cnn.close
    return invoice

def get_invoice_id2(id_user):
    cnn = get_connection()
    invoice2 = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT US.id_user,(select count(*) from dbbiblioteca.customer where id=US.id_user) customer FROM dbbiblioteca.invoice AS US WHERE US.id_user=%s",(id_user))
        invoice2 = cursor.fetchone()
        
    cnn.close
    return invoice2