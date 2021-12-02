from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask.wrappers import Request
import user_controller
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'Static/img'

app.secret_key = 'sdvfsd'

@app.route('/')

@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/newuser')
def newuser():
    return render_template('newuser.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == "POST":
        # capturar datos enviados por el templates login.html
        email = request.form['email']
        password = request.form['password']
        # creación de variables de sesión
        session['email'] = email
        session['password'] = password
        return redirect("/index_customer")

@app.route('/logout')
def logout():
    #Cerrar la session
    session.clear()
    return redirect("/index")


@app.route("/save_login", methods=["POST"])
def save_login():
    
    emailprueba = request.form["email"]
    #print (emailprueba)
    countemail = user_controller.get_email()
    print (countemail)
    
    for email2 in countemail:
        # print (email2[0])
        # print (emailprueba)
        if emailprueba == email2[0] :
            flash("El correo ya fue registrado")
            return redirect(url_for('index'))  
            #
    if request.method == 'POST':            
        f = request.files['ufile']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        name = request.form["name"]
        email = request.form["email"]
        password = request.form['password']
        
        user_controller.add_login(name,email,password)
        flash("El usuario ya fue registrado")
        return redirect("/index")
       
#----------------------------------------------------------------------------------------------

@app.route('/index_customer')
def index_customer():
    
    c = user_controller.get_count_users()
    #print(c[0])
    if c[0] >= 1:
        
        logins = user_controller.get_login()
        #print (users)
        for login in logins:
            #print (login)
            if session['email'] == login[2] and session['password'] == login[3]:
                users = user_controller.get_users()
                return render_template('index_customer.html',users=users,login=login)
        flash("La contraseña o el correo son incorrectos, INTENTE DE NUEVO")
        return redirect(url_for('index'))   
    else:
        flash("No existen usuarios registrados")
        return redirect(url_for('index'))
        
        
@app.route('/form_add_user')
def form_add_user():
    return render_template('add_user.html')

@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = user_controller.get_user_id(id)
    return render_template('edit_user.html',user = user)

@app.route('/update_user', methods=['POST'])
def update_user():
    # obtener los datos del formulario que invocó este end-point
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    movile = request.form['movile']
    user_controller.update_user(name,status,movile,id)
    return redirect('/index_customer')

@app.route("/delete_user", methods=["POST"])
def delete_user():  
    user_controller.delete_user(request.form["id"])
    return redirect("/index_customer")

@app.route("/save_user", methods=["POST"])
def save_user():
    name = request.form["name"]
    status = request.form["status"]
    movile = request.form['movile']
    user_controller.add_user(name,status,movile)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/index_customer")

#----------------------------------------------------------------------------------------------

@app.route('/index_invoice')
def index_invoice():
    invoices = user_controller.get_invoice()
    return render_template('index_invoice.html',invoices = invoices)

@app.route('/form_add_invoice')
def form_add_invoice():
    return render_template('add_invoice.html')

@app.route('/edit_invoice/<int:id>')
def edit_invoice(id):
    invoice = user_controller.get_invoice_id(id)
    return render_template('edit_invoice.html', invoice = invoice)

@app.route('/update_invoice', methods=['POST'])
def update_invoice():
    # obtener los datos del formulario que invocó este end-point
    id = request.form['id']
    number = request.form['number']
    date = request.form['date']
    price = request.form['price']
    balance = request.form['balance']
    user_controller.update_invoice(number, date, price,balance,id)
    return redirect('/index_invoice')

@app.route("/delete_invoice", methods=["POST"])
def delete_invoice():
    user_controller.delete_invoice(request.form["id"])
    return redirect("/index_invoice")

@app.route("/save_invoice", methods=["POST"])
def save_invoice():
    number = request.form["number"]
    date = request.form["date"]
    id_user = request.form['id_user']
    price = request.form['price']
    balance = request.form['balance']
    user_controller.add_invoice(number, date, id_user, price, balance)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/index_invoice")

if __name__ == "__main__":
    app.run(port = 4444, debug=True)