from . import products
from flask_security import login_required, roles_required, current_user
from flask import redirect, render_template, request, url_for

from ..models import Producto
from ..forms import ProductoForm
from ..main import db

@products.route('/')
@login_required
@roles_required('user')
def index():
    
    productos = Producto.query.all()
    
    context = {
        'p' : productos
    }
    
    return render_template('userProductos.html', **context)

@products.route('/admin')
@login_required
@roles_required('admin')
def admin():
    
    producto_form = ProductoForm()
    productos = Producto.query.all()
    
    context = {
        'form' : producto_form,
        'productos': productos
    }
    
    return render_template('adminProductos.html', **context)

@products.route('/admin/new', methods = ['POST'])
@login_required
@roles_required('admin')
def admin_new():
    
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    precio = request.form['precio']
    imagen = request.form['imagen']
    
    new_producto = Producto(nombre, cantidad, precio, imagen)
    
    db.session.add(new_producto)
    db.session.commit()
    
    return redirect(url_for('products.admin'))

@products.route('/admin/update/<id>', methods = ['GET','POST'])
@login_required
@roles_required('admin')
def update(id):
    
    producto = Producto.query.get(id)
    producto_form = ProductoForm()
    
    context = {
        'form' : producto_form,
        'p' : producto
    }
    
    if request.method == 'POST':
        
        producto.nombre = request.form['nombre']
        producto.cantidad = request.form['cantidad']
        producto.precio = request.form['precio']
        producto.imagen = request.form['imagen']
        
        db.session.commit()
        
        return redirect(url_for('products.admin'))
    
    return render_template('update.html', **context)


@products.route('/admin/delete/<id>')
@login_required
@roles_required('admin')
def delete(id):
    
    producto = Producto.query.get(id)
    
    db.session.delete(producto)
    db.session.commit()
    
    return redirect(url_for('products.admin'))

