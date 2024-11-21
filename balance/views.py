from . import app

@app.route('/')
def home():
         return ('Hola, balance')