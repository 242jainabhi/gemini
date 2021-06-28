import datetime

from application.constants import RoleEnum
from . import db
from application.models import user, workspace


class UserWorkspace(db.Model):
    __tablename__ = 'user_workspace'
    db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id'))
    db.Column('role', db.Enum(RoleEnum), default=RoleEnum.VIEWER)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship(user.User,
                           backref=db.backref('user_workspace',
                                              cascade="all, delete-orphan"))
    workspace = db.relationship(workspace.Workspace,
                                backref=db.backref('user_workspace',
                                                   cascade="all, delete-orphan"))
