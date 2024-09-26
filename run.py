from app import create_app, db
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table("veiculos"):
        # Cria as tabelas
        db.create_all()
        print("Tabelas criadas.")
    else:
        print("Tabelas já existem.")

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar o caminho das credenciais
credenciais_google = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

if not credenciais_google:
    raise RuntimeError("Credenciais do Google não configuradas.")

if __name__ == "__main__":
    app.run(debug=True)
