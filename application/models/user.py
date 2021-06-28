import datetime
from . import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), default='guest_user')
    email = db.Column(db.String(50), nullable=False, unique=True)
    organization = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    workspaces = db.relationship('Workspace', secondary='user_workspace')
    invitations = db.relationship('Invitation', backref='users')
