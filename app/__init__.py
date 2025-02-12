from flask import Flask
from flask_cors import CORS
from .core.config import Config
from .core.database import db, migrate
from .api import api_blueprint
from flasgger import Swagger
from flask_jwt_extended import JWTManager
import yaml


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)
    with open("swagger.yaml", "r") as file:
        swagger_template = yaml.safe_load(file)  
    Swagger(app, template=swagger_template)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app
