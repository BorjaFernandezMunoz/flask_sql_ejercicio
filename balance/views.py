from flask import render_template

from balance.models import ListaMovimientosDB, ListaMovimientosCSV

from . import app, ALMACEN


@app.route('/')
def home():
    if ALMACEN == 0:
        lista = ListaMovimientosCSV()
    else:
        lista = ListaMovimientosDB()
    return render_template('inicio.html', movs = lista.movimientos)


@app.route('/eliminar/<int:id>')
def delete(id):
    lista = ListaMovimientosDB()
    template = 'borrado.html'
   
    try:
        result = lista.eliminar(id)
        if not result:
            template = 'error.html'
    except:
        template = 'error.html'

    return render_template(template, id=id)