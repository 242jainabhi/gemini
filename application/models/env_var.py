from application import db
from datetime import datetime


class EnvVar(db.Model):
    __tablename__ = "env_var"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    value = db.Column(db.String(50), nullable=False)  #, unique=True)
    env_id = db.Column(db.Integer, db.ForeignKey('environment.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
