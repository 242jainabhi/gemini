from . import health_check_controller, user_controller, workspace_controller, invitation_controller


def initialize_routes(api):
    api.add_resource(health_check_controller.Health, '/health')
    api.add_resource(user_controller.User, '/user', '/user/<int:user_id>')
    api.add_resource(user_controller.Users, '/users')
    api.add_resource(workspace_controller.Workspace, '/workspace', '/workspace/<int:ws_id>')
    api.add_resource(workspace_controller.Workspaces, '/workspaces')
    api.add_resource(invitation_controller.Invitation, '/send_invite', '/accept_invite')
    # api.add_resource(invitation.Invitation, )
