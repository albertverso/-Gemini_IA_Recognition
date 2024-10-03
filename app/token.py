from functools import wraps
from flask import request, jsonify
import jwt
from config.config import Config
from app import create_app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Verificar se o token foi enviado no cabeçalho da requisição
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # "Bearer <token>"

        if not token:
            return jsonify({'message': 'Token é necessário!'}), 401

        try:
            # Decodificar o token
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_user_id = data['user_id']  # Pegar o ID do usuário do token
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirou!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido!'}), 401

        return f(current_user_id, *args, **kwargs)

    return decorated
