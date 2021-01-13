import os
from os.path import abspath, dirname
from dotenv import load_dotenv

APP_ROOT = dirname(dirname(abspath(__file__)))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

PROPAGATE_EXCEPTIONS = True

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE')

# configuracion de despligue de la aplicacion
DEBUG = False
TESTING = False
ENV = ''