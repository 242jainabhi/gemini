from datetime import datetime, timedelta
from . import db


class Invitation(db.Model):
    __tablename__ = 'invitation'
    current_time = datetime.utcnow()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)
    receiver_email = db.Column(db.String(50), nullable=False)
    invite_uuid = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=current_time, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    expired_at = db.Column(db.DateTime, nullable=False,
                           default=current_time + timedelta(days=2))
    utilized = db.Column(db.Boolean, default=False)
