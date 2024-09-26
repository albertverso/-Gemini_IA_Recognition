from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # Isso cria todas as tabelas definidas nos modelos
