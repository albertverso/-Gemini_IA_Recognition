from flask import Blueprint, request, jsonify
from app.models import Vehicle
from app import db
from app.db import adicionar_veiculo, buscar_veiculo_por_placa
from app.vision import generate_text_from_image

bp = Blueprint('routes', __name__)

@bp.route('/buscar_veiculo', methods=['POST'])
def buscar_veiculo():
    # Verificando se a imagem foi enviada
    if 'image' not in request.files:
        return jsonify({"error": "Image file is required"}), 400

    # Pegando a imagem do form data
    vehicle_image = request.files['image']
    
    # Gerando texto a partir da imagem
    vehicle_description = generate_text_from_image(vehicle_image)
   
    # Aqui você deve ter a lógica para verificar se o veículo existe no seu banco de dados
    vehicle = buscar_veiculo_por_placa(vehicle_description)  # Altere conforme necessário

    if vehicle:  # Se o veículo existe
        vehicle_data = vehicle.to_dict()  # Serializa o veículo para um dicionário
        return jsonify(vehicle_data), 200  # Retorna os dados do veículo
    else:
        return jsonify({"error": f"Veículo com placa: {vehicle_description} não encontrado"}), 404

@bp.route('/adicionar_veiculo', methods=['POST'])
def adicionar_novo_veiculo():
    """
    Rota para adicionar um novo veículo ao banco de dados.
    """
    data = request.get_json()

    placa = data.get('placa')
    modelo = data.get('modelo')
    cor = data.get('cor')
    ano = data.get('ano')
    dono = data.get('dono')

    if not placa or not modelo or not cor or not ano or not dono:
        return jsonify({"error": "Dados incompletos"}), 400

    adicionar_veiculo(placa, modelo, cor, ano, dono)

    return jsonify({"message": "Veículo adicionado com sucesso"}), 201