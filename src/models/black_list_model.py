from flask_marshmallow import sqla
from db import db

class BlackListModel(db.Model):
    __tablename__ = "BlackList"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    uuid = db.Column(db.Integer)
    reason = db.Column(db.String(255))
    ip = db.Column(db.String)
    date = db.Column(db.DateTime)

    @classmethod
    def find_email(cls, email):
        return cls.query.filter_by(
            email = email
        ).first()
    
class BlackListSchema(sqla.SQLAlchemyAutoSchema):
    class Meta:
        model = BlackListModel
        include_relationships = True
        load_instance = True