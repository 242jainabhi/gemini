import datetime
from application import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), default='guest_user')
    email = db.Column(db.String(50), nullable=False, unique=True)
    organization = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    workspaces = db.relationship("Workspace", secondary="user_workspace",
                                 backref=db.backref("users"))  #, cascade="all, delete-orphan"))
    invitations = db.relationship("Invitation", backref="users")
    environments = db.relationship("Environment", backref="creator")
