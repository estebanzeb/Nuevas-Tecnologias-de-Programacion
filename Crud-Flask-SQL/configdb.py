#Libreria para conexion a MySQl
import pymysql

#Metodo para realizar la conexion a mysql

def get_connection():
    return pymysql.connect(host='localhost', user='root', passwd='',
    db='dbbibliotk')