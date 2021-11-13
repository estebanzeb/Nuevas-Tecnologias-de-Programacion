from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask.wrappers import Request
import user_controller

app = Flask(__name__)
app.secret_key = 'sdvfsd'
@app.route('/')

@app.route('/index')
def index():
    return render_template('login.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')
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


@app.route('/index_customer')
def index_customer():
    if session['email'] == 'xx@gmail.com' and session['password'] == '11':
        users = user_controller.get_users()
        return render_template('index_customer.html',users=users)       
    else: 
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