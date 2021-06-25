from . import health_check, user, workspace


def initialize_routes(api):
    api.add_resource(health_check.Health, '/health')
    api.add_resource(user.User, '/user', '/user/<int:id>')
    api.add_resource(user.Users, '/users')
    api.add_resource(workspace.Workspace, '/workspace', '/workspace/<int:id>')
    api.add_resource(workspace.Workspaces, '/workspaces')
