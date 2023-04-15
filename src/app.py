from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from views.black_list_view import EmailSave, EmailSearch, AccessToken, ServiceHealth

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "Secreto"
jwt = JWTManager(app)

with app.app_context():
    import models

    db.create_all()

api.add_resource(EmailSave, "/blacklists")
api.add_resource(EmailSearch, "/blacklists/<string:email>")
api.add_resource(AccessToken, "/blacklists/token")
api.add_resource(ServiceHealth, "/blacklists/ping")
