import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

#load_dotenv()
# Instanciamos Flask
app = Flask(__name__) 

# Configuración correcta de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', '')

# Desactivar el rastreo de modificaciones (opcional, pero recomendable)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instanciamos SQLAlchemy
db = SQLAlchemy(app)

# Modelo de Taxi
class taxis(db.Model):
    """Modelo para la tabla 'taxis'
    - id: número único identificador para taxi
    - plate: placa del taxi (única)
    """
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10), unique=True, nullable=False)

    # Método to_dict para transformar el objeto en un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "plate": self.plate
        }

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

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
