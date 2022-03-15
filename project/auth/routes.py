from flask import render_template, redirect, url_for, request
from . import auth
from project.forms import LoginForm, RegistroForm

# Modulo para el cifrado del passwords
from werkzeug.security import generate_password_hash, check_password_hash

from flask_security import login_required
from flask_security.utils import login_user, logout_user
from project import db, userDataStore
from project.models import User


# Login - GET / POST
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    
    login_form = LoginForm()
    
    if request.method == 'POST':
        
        email = login_form.mail.data
        password = login_form.password.data
        
        # Consultamos si existe un usuario ya registrado con el email
        user = User.query.filter_by(email = email).first()
        
        # Verificamos si el usuario existe
        # Tomamos el password proporcionado por el usuario lo hasheamos, y lo comparamos con el password en la base de datos
        if not user or not check_password_hash(user.password, password):
            print('El usuario y/o contraseña son incorrectos')
            return redirect(url_for('auth.login')) # Si el usuario no existe o el password no coincide
        
        # Si llegamos a este punto sabemos que el usuario tiene datos correctos
        # Creamos la sesion y logeamos al usuario
        login_user(user)
        return redirect(url_for('main.index'))
    
    context = {
        'form' : login_form
    }
    
    return render_template('/auth/login.html', **context)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    
    
    registro_form = RegistroForm()
    
    if request.method == 'POST':
        usuario = registro_form.user.data
        email = registro_form.mail.data
        password = registro_form.password.data
        
        # Consultamos si existe un usuario ya registrado con ese email.
        user = User.query.filter_by(email = email).first()
        
        if user: # Si se encontró un usuario, redireccionamos de regreso al registro
            print('El correo electronico ya existe')
            return redirect(url_for('auth.register'))
        
        # Creamos un nuevo usuario con los datos del formulario
        # Hacemos un hash a la contraseña para que no se guarde la version en texto plano
        # new_user = User(email = email, name = name, password = generate_password_hash(password, method = 'sha256'))
        
        userDataStore.create_user(
            name = usuario,
            email = email,
            password = generate_password_hash(password, method = 'sha256')
        )
        
        # Añadimos el usuario a la BD
        # db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
        
    
    context = {
        'form' : registro_form
    }
    
    return render_template('/auth/register.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))