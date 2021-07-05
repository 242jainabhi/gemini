from application import db
from datetime import datetime


class Environment(db.Model):
    __tablename__ = "environment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    env_vars = db.relationship('EnvVar', backref='environment')
