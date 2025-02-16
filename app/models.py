import uuid
from app import db

class Kevin(db.Model):
    __tablename__ = 'kevin'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Kevin {self.nombre} {self.apellidos}>'