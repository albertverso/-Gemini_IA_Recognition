from app import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), unique=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Vehicle {self.license_plate}>'

    def to_dict(self):
        """Converte a instância do veículo em um dicionário."""
        return {
            'id': self.id,
            'license_plate': self.license_plate,
            'model': self.model,
            'color': self.color,
            'year': self.year,
            'owner': self.owner
        }

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # A senha deve ser criptografada
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        """Converte a instância do usuário em um dicionário."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at
        }

