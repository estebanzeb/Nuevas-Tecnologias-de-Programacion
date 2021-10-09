from flask import Flask, render_template,url_for,request,redirect
import Controler_users

app  = Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    users = Controler_users.get_user()
    return render_template('index.html', users = users)

@app.route('/form_add_users')
def form_add_users():
    return render_template('add_users.html')

@app.route('/edit_user/<int:id>')
def edit_users(id):
    users = Controler_users.get_user_id(id)
    return render_template('edit_user.html', users= users)
  
@app.route("/update_user", methods=["POST"])
def update_user():
    #obtener los datos del formulario que invoco este end-ponit
    id = request.form["id"]
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    password = request.form["password"]
    Controler_users.update_user( name, email, phone, password, id)
    return redirect("/")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(port=5300, debug=True)