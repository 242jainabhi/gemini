import datetime
from application import db


class Workspace(db.Model):
    __tablename__ = 'workspace'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    # users = db.relationship("User", secondary="user_workspace")
    invitations = db.relationship("Invitation", backref="workspaces")
    api_spaces = db.relationship("ApiSpace", backref="workspace")
    environments = db.relationship("Environment", backref="workspace")
