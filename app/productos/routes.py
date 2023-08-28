from flask import render_template
from app.productos import productos


@productos.route('/create')
def crear():
    return render_template('new.html')