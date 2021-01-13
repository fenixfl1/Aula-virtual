from flask_login import LoginManager
from flask_restful import Api


login_manager = LoginManager()
api = Api(catch_all_404s=True)