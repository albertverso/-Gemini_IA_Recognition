from app import db

class Vehicle(db.Model):
    __tablename__ = 'veiculos'

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(20), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    dono = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Veículo {self.placa}>'

    def to_dict(self):
        """Converte a instância do veículo em um dicionário."""
        return {
            'id': self.id,
            'placa': self.placa,
            'modelo': self.modelo,
            'cor': self.cor,
            'ano': self.ano,
            'dono': self.dono
        }

