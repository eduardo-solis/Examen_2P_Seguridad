import os
from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy

# Creamos una instancia de SQLAlchemy
db = SQLAlchemy()

# Creamos el SQLalchemyUserDataStore
from .models import User, Role
userDataStore = SQLAlchemyUserDatastore(db, User, Role)

# Método principal de la aplicación
def create_app():
    # Creamos una instancia de Flask
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Generamos la clave aleatoria de sesión Flask para crear una cookie con la info de la sesión
    app.config['SECRET_KEY'] = os.urandom(24)
    
    # Definimos la ruta a la BD: mysql://user:password@localhost/bd
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/bbtesta'
    
    app.config['SECURITY_PASSWORD_SALT'] = 'thisissecretsalt'
    
    db.init_app(app)
    @app.before_first_request
    def create_all():
        db.create_all()
    
    # Conectamos los modelos a flask-security
    security = Security(app,userDataStore)
    
    # Registramos el blueprint para las rutas no auth
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Registramos el blueprint para las rutas de auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # Registramos el blueprint para las rutas de products
    from .products import products as products_blueprint
    app.register_blueprint(products_blueprint)
    
    return app
