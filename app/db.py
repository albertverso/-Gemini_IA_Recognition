from app.models import Vehicle
from app import db

def adicionar_veiculo(placa, modelo, cor, ano, dono):
    novo_veiculo = Vehicle(placa=placa, modelo=modelo, cor=cor, ano=ano, dono=dono)
    db.session.add(novo_veiculo)
    db.session.commit()

def buscar_veiculo_por_placa(placa):
    return Vehicle.query.filter_by(placa=placa).first()
