import enum
from .. import db


class RoleEnum(enum.Enum):
    ADMIN = 'admin'
    VIEWER = 'viewer'
    CONTRIBUTOR = 'contributor'
    COMMENTER = 'commenter'


user_workspace = db.Table('user_workspace',
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                          db.Column('workspace_id', db.Integer, db.ForeignKey('workspace.id'))
                          )
                          # db.Column('role', db.Enum(RoleEnum)))