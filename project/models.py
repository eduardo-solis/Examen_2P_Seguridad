from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

# Definimos la tabla relacional
users_roles = db.Table('users_roles',
                        db.Column('userId', db.Integer, db.ForeignKey('user.id')),
                        db.Column('roleId', db.Integer, db.ForeignKey('role.id'))
                        )


# Definimos la clase del usuario
class User(UserMixin, db.Model):
    ''' User account model '''
    
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100), nullable = False)
    
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role', 
                            secondary = users_roles, 
                            backref = db.backref('users', lazy = 'dynamic'))
    
class Role(RoleMixin, db.Model):
    '''Role model'''
    
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(255))

class Producto (db.Model):
    
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    cantidad = db.Column(db.Integer, nullable = False)
    precio = db.Column(db.Float, nullable = False)
    imagen = db.Column(db.String(100), nullable = False)
    
    def __init__(self, nombre, cantidad, precio, imagen):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.imagen = imagen
    