from application import db
from datetime import datetime


class Api(db.Model):
    __tablename__ = "api"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    api_space_id = db.Column(db.Integer, db.ForeignKey('api_space.id'))
    # endpoint
    # url
    # method
    # author
    # parameters
    # header
    # body
    specification = db.Column(db.JSON)  # TBD

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
