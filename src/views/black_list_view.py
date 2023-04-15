from flask import request
from flask_restful import Resource
from datetime import datetime
from flask_jwt_extended import jwt_required, create_access_token

from models import BlackListModel, BlackListSchema
from db import db

black_list_schema = BlackListSchema()

class EmailSave(Resource):
    
    @jwt_required()
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

    @jwt_required()
    def get(self, email):
        email_search = BlackListModel.find_email(email)
        if email_search is None:
            return {"Status": False},200
        else:
            message = black_list_schema.dump(email_search)
            return {"Status": True, "Blocked reason": message["reason"]}, 200
        
class AccessToken(Resource):

    def post(self):
        access_token = create_access_token('secreto')
        return {"Token": access_token}, 200

class ServiceHealth(Resource):

    def get(self):
        return ("pong")