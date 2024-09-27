from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    """
    Fun o que cria o app Flask.
    Carrega as configura es da classe Config,
    inicializa o SQLAlchemy com o app Flask e
    registra as rotas.
    """
    app = Flask(__name__)

    CORS(app)

    # Carregar configura es da classe Config
    app.config.from_object(Config)

    # Inicializar SQLAlchemy com o app Flask
    db.init_app(app)

    # Registro de blueprints e rotas aqui
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app

