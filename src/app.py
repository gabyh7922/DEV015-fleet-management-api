from init import app
from models import taxis


# Definir las rutas
@app.route('/')
def index():
    return 'Conociendo el alcance de Flask'

@app.route('/taxis')
def list_taxis():
    # Obtener todos los taxis de la base de datos
    taxis_list = taxis.query.all()
    return {
        "taxis": [taxi.to_dict() for taxi in taxis_list]
    }

if __name__ == '__main__':
    app.run(debug=True)
