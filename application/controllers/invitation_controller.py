import uuid
from datetime import datetime, timedelta
from flask import request, make_response, jsonify
from flask_restful import Resource

from application.constants import RoleEnum
from application.models import user, invitation, user_workspace
from application.services.user_service import UserService
from application.services.workspace_service import WorkspaceService
from application.services.invitation_service import InvitationService
from application.services.user_workspace_service import UserWSService


class Invitation(Resource):

    def get(self):
        invite_uuid = request.args.get('uuid')
        inv = InvitationService().get_invitation_by_uuid(invite_uuid)
        InvitationService().update_invite_utilized(inv)

        # add record in user table
        # append this user to the workspace.users list
        user_obj = user.User(email=inv.receiver_email)
        UserService().add_user(user_obj)

        u_ws_obj = user_workspace.UserWorkspace(user_id=user_obj.id,
                                                workspace_id=inv.workspace_id,
                                                role=RoleEnum.CONTRIBUTOR)
        resp = UserWSService().add_association(u_ws_obj)

        return 'Accept invite success'

    def post(self):
        data = request.get_json()
        sender_id = data['sender_id']
        workspace_id = data['workspace_id']
        # receiver_name = data['receiver_name']
        receiver_email = data['receiver_email']
        # receiver_organization = data['receiver_organization']

        # user_obj = user.User(name=receiver_name, email=receiver_email,
        #                      organization=receiver_organization)
        invite_uuid = uuid.uuid4()
        invitation_obj = invitation.Invitation(
            sender_id=sender_id, workspace_id=workspace_id,
            receiver_email=receiver_email, invite_uuid=invite_uuid)
        # invitation_obj.expired_at = invitation_obj.created_at + timedelta(days=2)
        InvitationService().add_invitation(invitation_obj)
        # us.UserService().add_user(user_obj)

        InvitationService().send_invitation_mail(invitation_obj)

        return 'Invite sent successfully' # make_response(jsonify(data), 200)

    # def put(self, user_id):
    #     u = UserService().get_user(user_id)
    #     data = request.get_json()
    #     resp = UserService().update_user(u, data)
    #     if resp:
    #         return "User updated successfully"
    #
    # def delete(self, user_id):
    #     u = UserService().get_user(user_id)
    #     UserService().delete_user(u)
    #     return f"Deleted user with id: {user_id}"
