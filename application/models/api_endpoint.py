from application import db
from datetime import datetime


class ApiEndpoint(db.Model):
    __tablename__ = "api_endpoint"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    endpoint = db.Column(db.String(50), nullable=False, unique=True)
    method = db.Column(db.String(50), nullable=False)
    api_space_id = db.Column(db.Integer, db.ForeignKey('api_space.id'))
    author_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # parameters
    # header
    # body
    # specification = db.Column(db.JSON)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
