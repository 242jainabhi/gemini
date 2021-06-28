import uuid
from datetime import datetime, timedelta
from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models import user, invitation
from application.services import user_service as us, workspace_service as ws, invitation_service as invs
from application.utils import send_invite


class Invitation(Resource):

    def get(self):
        invite_uuid = request.args.get('uuid')
        inv = invs.InvitationService().get_invitation_by_uuid(invite_uuid)

        # update user table

        w = ws.WorkspaceService().get_workspace(inv.workspace_id)
        w.users.append()
        # update user_workspace table with this user as 'Contributor'
        # append this user to the workspace.users list

    def post(self):
        data = request.get_json()
        sender_id = data['sender_id']
        workspace_id = data['workspace_id']
        receiver_name = data['receiver_name']
        receiver_email = data['receiver_email']
        receiver_organization = data['receiver_organization']

        # user_obj = user.User(name=receiver_name, email=receiver_email,
        #                      organization=receiver_organization)
        invite_uuid = uuid.uuid4()
        invitation_obj = invitation.Invitation(
            sender_id=sender_id, workspace_id=workspace_id,
            receiver_email=receiver_email, invite_uuid=invite_uuid)
        # invitation_obj.expired_at = invitation_obj.created_at + timedelta(days=2)
        invs.InvitationService().add_invitation(invitation_obj)
        # us.UserService().add_user(user_obj)

        # move this to service
        # trigger the mail to receiver_email with the body (f'/accept_invite?uuid={invite_uuid}')
        u = us.UserService().get_user(sender_id)
        w = ws.WorkspaceService().get_workspace(workspace_id)
        sender_name = u.name
        sender_mail = u.email
        invite_link = f'https://localhost:5000/accept_invite?uuid={invite_uuid}'
        send_invite.SendInvite(sender_name, sender_mail, receiver_email,
                               invite_link).send_mail()

        return 'Success' # make_response(jsonify(data), 200)

    def put(self, user_id):
        u = us.UserService().get_user(user_id)
        data = request.get_json()
        resp = us.UserService().update_user(u, data)
        if resp:
            return "User updated successfully"

    def delete(self, user_id):
        u = us.UserService().get_user(user_id)
        us.UserService().delete_user(u)
        return f"Deleted user with id: {user_id}"
