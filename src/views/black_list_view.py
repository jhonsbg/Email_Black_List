from flask import request
from flask_restful import Resource
from datetime import datetime

from models import BlackListModel, BlackListSchema
from db import db

black_list_schema = BlackListSchema()

class EmailSave(Resource):

    def post(self):
        new_email = BlackListModel(
            email = request.json["email"],
            uuid = request.json["app_uuid"],
            reason = request.json["blocked_reason"],
            ip = request.headers.get('X-Forwarded-For', request.remote_addr),
            date = datetime.now()
        )

        try:
            db.session.add(new_email)
            db.session.commit()
            return {'message': 'Correo electrónico guardado correctamente'}, 201
        except:
            db.session.rollback()
            return {'message': 'Error al guardar el correo electrónico'}, 500

class EmailSearch(Resource):

    def get(self, email):
        email_search = BlackListModel.find_email(email)
        if email_search is None:
            return {"Status": False},200
        else:
            message = black_list_schema.dump(email_search)
            return {"Status": True, "Blocked reason": message["reason"]}, 200