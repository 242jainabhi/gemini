from . import health_check_controller, user_controller, workspace_controller, \
    invitation_controller, api_space_controller, environment_controller, env_var_controller, \
    api_endpoint_controller


def initialize_routes(api):
    api.add_resource(health_check_controller.Health, '/health')
    api.add_resource(user_controller.UserController, '/user/<int:user_id>', '/user')
    api.add_resource(user_controller.Users, '/users')
    api.add_resource(workspace_controller.WorkspaceController, '/workspace/<int:ws_id>', '/workspace')
    api.add_resource(workspace_controller.Workspaces, '/workspaces')
    api.add_resource(invitation_controller.Invitation, '/send_invite', '/accept_invite')
    api.add_resource(api_space_controller.ApiSpaceController, '/api_space/<int:api_space_id>', '/api_space')
    api.add_resource(api_space_controller.ApiSpacesController, '/api_spaces')
    api.add_resource(environment_controller.EnvironmentController, '/environment/<int:env_id>', '/environment')
    api.add_resource(environment_controller.EnvironmentsController, '/environments')
    api.add_resource(env_var_controller.EnvVarController, '/env_var/<int:env_var_id>', '/env_var')
    api.add_resource(env_var_controller.EnvVarsController, '/env_vars')
    api.add_resource(api_endpoint_controller.ApiEndpointController, '/api_endpoint/<int:api_endpoint_id>', '/api_endpoint')
    api.add_resource(api_endpoint_controller.ApiEndpointsController, '/api_endpoints')

    # api.add_resource(invitation.Invitation, )
