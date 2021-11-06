#paquete para el manejo del sistema operativo
import os
from flask import Flask, render_template, redirect, request, flash
from werkzeug.utils import secure_filename #guardar informacion en el sistema operativo

app = Flask(__name__)

#configurar la carpeta para almacenar los archivos
app.config['UPLOAD_FOLDER'] = 'Static/Image'

app.secret_key = '_5#y2L"F4Q8z\xec]/'

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['ufile']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        flash("La archivo se a subido correctamente..")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=4500)
