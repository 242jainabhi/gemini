import datetime

from application.models import invitation
from sqlalchemy import exc
from application import db


class InvitationService:
    def __init__(self):
        pass

    def get_invitation(self, invitation_id):
        inv = invitation.Invitation.query.filter_by(id=invitation_id).first()
        if not inv:
            raise Exception("Invitation not found")

        return inv

    def get_invitation_by_uuid(self, uuid):
        inv = invitation.Invitation.query.filter_by(invite_uuid=uuid).first()
        if not inv:
            raise Exception("Invitation not found")
        if inv.deleted_at is not None:
            raise Exception('Invitation Deleted!')
        if inv.expired_at < datetime.utcnow():
            raise Exception('Invitation Expired!')

        try:
            inv.utilized = True
            db.session.commit()
        except:
            raise Exception("Error updating the invitation data", e)

        return inv

    def add_invitation(self, invitation_obj):
        try:
            db.session.add(invitation_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Invitation not added', e)
        else:
            return True

    # def update_user(self, user_obj, data):
    #     for k, v in data.items():
    #         setattr(user_obj, k, v)
    #
    #     try:
    #         db.session.commit()
    #     except exc.IntegrityError as e:
    #         raise Exception("Error updating the user", e)
    #     else:
    #         return True

    # def delete_user(self, user_obj):
    #     user_obj.deleted_at = datetime.datetime.utcnow()
    #     try:
    #         db.session.commit()
    #     except:
    #         raise Exception('Can not deleted user')
