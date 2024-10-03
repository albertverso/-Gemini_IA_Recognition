from app import create_app, db
from sqlalchemy import inspect, text

app = create_app()

with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table("vehicles", "users"):
        # Cria as tabelas
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
