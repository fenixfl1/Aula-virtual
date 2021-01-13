from flask import Flask
from flask_cors import CORS
from .ext import login_manager
from app.api import api_bp

def create_app(setting_module=None):
    
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_object(setting_module)
    
    if not app.config.get('TESTING'):
        app.config.from_envvar('APP_PRODUCTION_SETTINGS', silent=True)
    else:
        app.config.from_envvar('APP_DEVELOPMENT_SETTINGS', silent=True)
    
    # Integracion de librerias
    CORS(app)
    login_manager.init_app(app)
    
    # Integrancion de planos
    app.register_blueprint(api_bp)
    
    return app