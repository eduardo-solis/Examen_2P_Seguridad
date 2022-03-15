from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DecimalField, FileField


class LoginForm(FlaskForm):
    
    mail = StringField('Correo')
    password = PasswordField('Contraseña')
    submit = SubmitField('Login')
    

class RegistroForm(FlaskForm):
    
    user = StringField('Usuario')
    mail = StringField('Correo')
    password = PasswordField('Contraseña')
    submit = SubmitField('Registrarse')
    

class ProductoForm(FlaskForm):
    
    nombre = StringField('Nombre')
    cantidad = IntegerField('Cantidad')
    precio = DecimalField('Precio')
    enviar = SubmitField('Guardar')
    imagen = FileField('Imagen')