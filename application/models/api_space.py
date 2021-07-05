from application import db
from datetime import datetime


class ApiSpace(db.Model):
    __tablename__ = "api_space"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'))
    documentation = db.Column(db.TEXT)  # TBD

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    api = db.relationship('Api', backref='api_space', uselist=False)
