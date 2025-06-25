from flask import Flask 
from app.routes import geogen_bp

def create_app():
    app = Flask(__name__)

    #enregistrer les blueprints
    app.register_blueprint(geogen_bp)

    return app