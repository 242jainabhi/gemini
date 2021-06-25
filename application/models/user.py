from . import db
from .association import associations


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    organization = db.Column(db.String(20))
    deleted_at = db.Column(db.DateTime, nullable=True)

    workspaces = db.relationship('Workspace', secondary=associations.user_workspace,
                                 back_populates='users')
