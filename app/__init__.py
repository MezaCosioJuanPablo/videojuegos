from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa y registra las rutas
    from .routes import main
    app.register_blueprint(main)

    return app
