import enum


class RoleEnum(enum.Enum):
    ADMIN = 'admin'
    VIEWER = 'viewer'
    CONTRIBUTOR = 'contributor'
    COMMENTER = 'commenter'
