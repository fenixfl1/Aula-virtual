from flask import Blueprint
from app.ext import api
from .resources.login import Login
from .common.routes import * 

api_bp = Blueprint('api_bp', __name__)
api.init_app(api_bp)

api.add_resource(Login, LOGIN_PATH)