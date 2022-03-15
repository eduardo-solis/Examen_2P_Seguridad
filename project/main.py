from flask import Blueprint, render_template
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from . import db


# Creamos el Blueprint
main = Blueprint('main', __name__)

# Definimos la ruta de la pagina principal
@main.route('/')
def index():
    return render_template('principal.html')

@main.route('/contacto')
def contacto():
    return render_template('contacto.html')


