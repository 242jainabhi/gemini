from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models.api_space import ApiSpace
from application.services.api_space_service import ApiSpaceService


class ApiSpaceController(Resource):
    # @app.route('/api_space/<int:id>', methods=['GET'])
    def get(self, api_space_id):
        space = ApiSpaceService().get_api_space(api_space_id)
        resp = {'id': space.id, 'name': space.name,
                'documentation': space.documentation,
                'workspaces': space.workspace.name}
        return make_response(jsonify(resp), 200)


    # @app.route('/api_space', methods=['POST'])
    def post(self):
        data = request.get_json()
        name = data['name']
        workspace_id = data['workspace_id']
        documentation = data['documentation']
        api_space_obj = ApiSpace(name=name, workspace_id=workspace_id, documentation=str(documentation))
        response = ApiSpaceService().add_api_space(api_space_obj)
        if response:
            data['id'] = api_space_obj.id
            return make_response(jsonify(data), 200)


    # @app.route('/api_space/id', methods=['PUT'])
    def put(self, api_space_id):
        api_space = ApiSpaceService().get_api_space(api_space_id)
        data = request.get_json()
        print(data)
        return ApiSpaceService().update_api_space(api_space, data)


    # @app.route('/api_sapce/id', methods=['DELETE'])
    def delete(self, api_space_id):
        api_space_obj = ApiSpaceService().get_api_space(api_space_id)
        return ApiSpaceService().delete_api_space(api_space_obj)


class ApiSpacesController(Resource):
    # @app.route('/api_spaces', methods=['GET'])
    def get(self):
        api_sapces = ApiSpaceService().get_all_api_spaces()
        resp = {}
        for api_space in api_sapces:
            resp[api_space.id] = {'name': api_space.name,
                                  'documentation': api_space.documentation,
                                  'workspace': api_space.workspace.name}
            # return u.id, u.name, u.email, u.organization
        return make_response(jsonify(resp), 200)
