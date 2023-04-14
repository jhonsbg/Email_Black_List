from flask import Flask
from flask_restful import Api

from db import db
from views.black_list_view import EmailSave, EmailSearch

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)
api = Api(app)

with app.app_context():
    import models

    db.create_all()

api.add_resource(EmailSave, "/blacklists")
api.add_resource(EmailSearch, "/blacklists/<string:email>")