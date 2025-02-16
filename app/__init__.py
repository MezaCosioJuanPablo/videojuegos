from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # 🔹 Forzar la conexión con MySQL al iniciar la app
    with app.app_context():
        try:
            db.engine.connect()
            print("✅ Conexión exitosa a la base de datos MySQL")
        except Exception as e:
            print(f"❌ Error conectando a MySQL: {e}")

    from .routes import main
    app.register_blueprint(main)

    return app