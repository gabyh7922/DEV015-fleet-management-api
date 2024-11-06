import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#load_dotenv()
# Instanciamos Flask
app = Flask(__name__) 
# Instanciamos SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', '')
# Desactivar el rastreo de modificaciones (opcional, pero recomendable)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()