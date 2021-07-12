from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models.api_endpoint import ApiEndpoint
from application.services.api_endpoint_service import ApiEndpointService


class ApiEndpointController(Resource):
    def __init__(self):
        self.service = ApiEndpointService()

    # @app.route('/api_space/<int:id>', methods=['GET'])
    def get(self, api_endpoint_id):
        endpoint = self.service.get_api_endpoint(api_endpoint_id)
        resp = {'id': endpoint.id, 'endpoint': endpoint.endpoint,
                'method': endpoint.method,
                'api_space': endpoint.api_space.name,
                'author': endpoint.author.name}
        return make_response(jsonify(resp), 200)

    # @app.route('/api_space', methods=['POST'])
    def post(self):
        data = request.get_json()
        endpoint = data['endpoint']
        method = data['method']
        api_space_id = data['api_space_id']
        author_user_id = data['author_user_id']
        '''
        documentation = data['documentation']
        we are not expecting documentation during api_space cration.
        It will be added after api_space creation, and will be an update operation.
        '''
        api_endpoint_obj = ApiEndpoint(endpoint=endpoint, method=method, api_space_id=api_space_id,
                                       author_user_id=author_user_id)
        response = self.service.add_api_endpoint(api_endpoint_obj)
        if response:
            data['id'] = api_endpoint_obj.id
            return make_response(jsonify(data), 200)

    # @app.route('/api_space/id', methods=['PUT'])
    def put(self, api_endpoint_id):
        api_endpoint = self.service.get_api_endpoint(api_endpoint_id)
        data = request.get_json()
        print(data)
        return self.service.update_api_endpoint(api_endpoint, data)

    # @app.route('/api_sapce/id', methods=['DELETE'])
    def delete(self, api_endpoint_id):
        api_endpoint_obj = self.service.get_api_endpoint(api_endpoint_id)
        return self.service.delete_api_endpoint(api_endpoint_obj)


class ApiEndpointsController(Resource):
    def __init__(self):
        self.service = ApiEndpointService()

    # @app.route('/api_spaces', methods=['GET'])
    def get(self):
        api_endpoints = self.service.get_all_api_endpoints()
        resp = {}
        for api_endpoint in api_endpoints:
            resp[api_endpoint.id] = {'endpoint': api_endpoint.endpoint,
                                     'method': api_endpoint.method,
                                     'api_sapce': api_endpoint.api_space.name,
                                     'author': api_endpoint.author.name}
        return make_response(jsonify(resp), 200)
