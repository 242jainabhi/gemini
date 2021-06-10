from .health_check import Health


def initialize_routes(api):
    api.add_resource(Health, '/health')
