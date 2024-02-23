from wtforms import Form
from wtforms import StringField, IntegerField,TextAreaField, SelectField,RadioField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='ingrese nombre valido')
        ])
    email=EmailField('correo',
                      [validators.Email('INGRESE UN EMAIL VALIDO')])
    apaterno=StringField('apaterno')
    amaterno=StringField('materno')
    edad=IntegerField('edad',
                      [validators.number_range(min=1, max=20,message='valor no valido')])
    materias=SelectField(choices=[('España','Esp',),('Mat','Matematicas'),
                                  ('Ingles','ING')])
    radios=RadioField('curso',choices=[("1","1"),("2","2"),("3","3")])


    '''
    FormulariosConClase
    '''

