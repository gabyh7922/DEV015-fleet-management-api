from init import db


# Modelo de Taxi
class taxis(db.Model):
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10), unique=True, nullable=False)

    # Método to_dict para transformar el objeto en un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "plate": self.plate
        }

