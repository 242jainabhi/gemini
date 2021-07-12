from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models.environment import Environment
from application.services.environment_service import EnvironmentService


class EnvironmentController(Resource):
    def __init__(self):
        self.service = EnvironmentService()

    def get(self, env_id):
        env = self.service.get_environment(env_id)
        resp = {'id': env.id, 'name': env.name,
                'creator': env.creator.name,
                'workspace': env.workspace.name}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        creator_id = data['creator_id']
        workspace_id = data['workspace_id']
        env_obj = Environment(name=name, creator_id=creator_id, workspace_id=workspace_id)
        response = self.service.add_environment(env_obj)
        if response:
            data['id'] = env_obj.id
            return make_response(jsonify(data), 200)

    def put(self, env_id):
        env = self.service.get_environment(env_id)
        data = request.get_json()
        print(data)
        return self.service.update_environment(env, data)

    def delete(self, env_id):
        env_obj = self.service.get_environment(env_id)
        return self.service.delete_environment(env_obj)


class EnvironmentsController(Resource):
    def __init__(self):
        self.service = EnvironmentService()

    def get(self):
        envs = self.service.get_all_envs()
        resp = {}
        for env in envs:
            resp[env.id] = {'name': env.name,
                            'creator': env.creator.name,
                            'workspace': env.workspace.name}
        return make_response(jsonify(resp), 200)
