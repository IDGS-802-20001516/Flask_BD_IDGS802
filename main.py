from flask import Flask, request,render_template, Response
import forms
from flask_wtf.csrf import CSRFProtect
from flask import flash
from models import db
from config import DevelopmentConfig

app=Flask(__name__)
app.secret_key ='esta es la clave secreta'

app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
        return render_template("index.html")

@app.before_request
def before_request():
    g.prueba ='Hola'
    print('antes de ruta')



@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
        print('dentro de alumnos')
        valor=g.prueba
        print('El dato es: {}'.format(valor))
        nom=''
        apa=''
        correo=''
        flash=''
        alumn_form=forms.UserForm(request.form)
        if request.method=="POST" and alumn_form.validate():
                nom=alumn_form.nombre.data
                apa=alumn_form.apaterno.data
                correo=alumn_form.email.data
                messages = 'Bienvenido {}'.format(nom)
                flash(messages)

                print("nombre:{}".format(nom))
                print("apaterno:{}".format(apa))
                print("apaterno:{}".format(correo))
                messages = 'Bienvenido {}'.format(nom)
                flash(messages)
        return render_template("alumnos.html", form=alumn_form,nom=nom,apa=apa,correo=correo)

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
          db.create_all()
    app.run()