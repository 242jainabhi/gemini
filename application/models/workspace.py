import datetime
from . import db
from .association import associations


class Workspace(db.Model):
    __tablename__ = 'workspace'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    users = db.relationship('User', secondary=associations.user_workspace,
                            back_populates='workspaces')