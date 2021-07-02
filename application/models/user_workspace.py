import datetime

from application.constants import RoleEnum
from application import db
from application.models.user import User
from application.models.workspace import Workspace


class UserWorkspace(db.Model):
    __tablename__ = "user_workspace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'))
    role = db.Column(db.Enum(RoleEnum), default=RoleEnum.VIEWER)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=True,
                           onupdate=datetime.datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    # user = db.relationship(User,
    #                        backref=db.backref("user_workspace",
    #                                           cascade="all, delete-orphan"))
    # workspace = db.relationship(Workspace,
    #                             backref=db.backref("user_workspace",
    #                                                cascade="all, delete-orphan"))
