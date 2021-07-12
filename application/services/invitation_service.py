from datetime import datetime

from sqlalchemy import exc
from application import db
from application.models.invitation import Invitation
from application.services.user_service import UserService
from application.services.workspace_service import WorkspaceService
from application.utils import send_invite


class InvitationService:
    def __init__(self):
        self.model = Invitation
        self.user_service = UserService()
        self.ws_service = WorkspaceService()

    def get_invitation(self, invitation_id):
        inv = self.model.query.filter_by(id=invitation_id).first()
        if not inv:
            raise Exception("Invitation not found")

        return inv

    def get_invitation_by_uuid(self, uuid):
        inv = self.model.query.filter_by(invite_uuid=uuid).first()
        if not inv:
            raise Exception("Invitation not found")
        if inv.deleted_at is not None:
            raise Exception('Invitation Deleted!')
        if inv.expired_at < datetime.utcnow():
            raise Exception('Invitation Expired!')

        return inv

    def update_invite_utilized(self, inv_obj):
        if inv_obj.utilized:
            # raising exception is not advised. Handle it in better way
            raise Exception("The invitation already accepted")
        try:
            inv_obj.utilized = True
            # inv_obj.updated_at = datetime.utcnow()
            db.session.commit()
        except:
            raise Exception("Error updating the invitation data", e)

        return True

    def add_invitation(self, invitation_obj):
        try:
            db.session.add(invitation_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Invitation not added', e)
        else:
            return True

    def send_invitation_mail(self, invitation_obj):
        # move this to service
        # trigger the mail to receiver_email with the body (f'/accept_invite?uuid={invite_uuid}')
        u = self.user_service.get_user(invitation_obj.sender_id)
        w = self.ws_service.get_workspace(invitation_obj.workspace_id)
        sender_name = u.name
        sender_mail = u.email
        invite_link = f'http://localhost:5000/accept_invite?uuid={invitation_obj.invite_uuid}'
        send_invite.SendInvite(sender_name, sender_mail, invitation_obj.receiver_email,
                               invite_link).send_mail()

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
