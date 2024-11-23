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