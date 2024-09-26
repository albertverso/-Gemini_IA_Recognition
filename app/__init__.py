from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

db = SQLAlchemy()

def create_app():
    """
    Fun o que cria o app Flask.
    Carrega as configura es da classe Config,
    inicializa o SQLAlchemy com o app Flask e
    registra as rotas.
    """
    app = Flask(__name__)

    # Carregar configura es da classe Config
    app.config.from_object(Config)

    # Inicializar SQLAlchemy com o app Flask
    db.init_app(app)

    # Registro de blueprints e rotas aqui
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app

