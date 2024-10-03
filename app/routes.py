from flask import Blueprint, request, jsonify
from app.models import Vehicle, User
from app import db
from app.db import add_vehicle, search_vehicle_by_plate, existing_vehicle
from app.vision import generate_text_from_image
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from config.config import Config
from .token import token_required

bp = Blueprint('routes', __name__)

@bp.route('/buscar_veiculo', methods=['POST'])
def search_vehicle():
    # Verificando se a imagem foi enviada
    if 'image' not in request.files:
        return jsonify({"error": "Image file is required"}), 400

    # Pegando a imagem do form data
    vehicle_image = request.files['image']
    
    # Gerando texto a partir da imagem
    vehicle_description = generate_text_from_image(vehicle_image)
   
    # Aqui você deve ter a lógica para verificar se o veículo existe no seu banco de dados
    vehicle = search_vehicle_by_plate(vehicle_description)  # Altere conforme necessário

    if vehicle:  # Se o veículo existe
        vehicle_data = vehicle.to_dict()  # Serializa o veículo para um dicionário
        return jsonify(vehicle_data), 200  # Retorna os dados do veículo
    else:
        return jsonify({"error": f"Veículo com placa: {vehicle_description} não encontrado"}), 404

@bp.route('/adicionar_veiculo', methods=['POST'])
@token_required
def add_new_vehicle(current_user_id):
    """
    Rota para adicionar um novo veículo ao banco de dados.
    """
    data = request.get_json()

    license_plate = data.get('license_plate')
    model = data.get('model')
    color = data.get('color')
    year = data.get('year')
    owner = data.get('owner')

    if not license_plate or not model or not color or not year or not owner:
        return jsonify({"error": "Dados incompletos"}), 400

    existing_vehicle_plate = existing_vehicle(license_plate)
    if existing_vehicle_plate:
        return jsonify({"error": "Veículo ja existe"}), 409

    add_vehicle(license_plate, model, color, year, owner)

    return jsonify({"message": "Veículo adicionado com sucesso"}), 201

@bp.route('/loadingAPI', methods=['GET'])
def loadingAPI():
    return jsonify({"message": "API carregada com sucesso"}), 200

@bp.route('/usuarios', methods=['POST'])
def create_user():
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Check if the email is already registered
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email já registrado.'}), 400

    # Hash the password
    password_hash = generate_password_hash(password)

    # Create the new user
    new_user = User(name=name, email=email, password=password_hash)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Usuário criado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Erro ao criar o usuário.', 'error': str(e)}), 500


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # Check if the user exists
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):  # Verifique a senha do usuário
        # Gerar o token JWT com uma chave secreta e tempo de expiração
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token válido por 1 hora
        }, Config.SECRET_KEY, algorithm="HS256")

        return jsonify({'token': token}), 200

    return jsonify({'error': 'Credenciais inválidas'}), 401

   
