from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models.api_space import ApiSpace
from application.services.api_space_service import ApiSpaceService


class ApiSpaceController(Resource):
    def __init__(self):
        self.service = ApiSpaceService()

    # @app.route('/api_space/<int:id>', methods=['GET'])
    def get(self, api_space_id):
        space = self.service.get_api_space(api_space_id)
        resp = {'id': space.id, 'name': space.name,
                'documentation': space.documentation,
                'workspaces': space.workspace.name}
        return make_response(jsonify(resp), 200)

    # @app.route('/api_space', methods=['POST'])
    def post(self):
        data = request.get_json()
        name = data['name']
        workspace_id = data['workspace_id']
        '''
        documentation = data['documentation']
        we are not expecting documentation during api_space cration.
        It will be added after api_space creation, and will be an update operation.
        '''
        api_space_obj = ApiSpace(name=name, workspace_id=workspace_id)  #, documentation=str(documentation))
        response = self.service.add_api_space(api_space_obj)
        if response:
            data['id'] = api_space_obj.id
            return make_response(jsonify(data), 200)

    # @app.route('/api_space/id', methods=['PUT'])
    def put(self, api_space_id):
        api_space = self.service.get_api_space(api_space_id)
        data = request.get_json()
        print(data)
        return self.service.update_api_space(api_space, data)

    # @app.route('/api_sapce/id', methods=['DELETE'])
    def delete(self, api_space_id):
        api_space_obj = self.service.get_api_space(api_space_id)
        return self.service.delete_api_space(api_space_obj)


class ApiSpacesController(Resource):
    def __init__(self):
        self.service = ApiSpaceService()

    # @app.route('/api_spaces', methods=['GET'])
    def get(self):
        api_sapces = self.service.get_all_api_spaces()
        resp = {}
        for api_space in api_sapces:
            resp[api_space.id] = {'name': api_space.name,
                                  'documentation': api_space.documentation,
                                  'workspace': api_space.workspace.name}
        return make_response(jsonify(resp), 200)
