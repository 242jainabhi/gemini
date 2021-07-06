from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models.env_var import EnvVar
from application.services.env_var_service import EnvVarService


class EnvVarController(Resource):
    def __init__(self):
        self.service = EnvVarService()
        # self.model = EnvVar

    def get(self, env_var_id):
        env_var = self.service.get_env_var(env_var_id)
        resp = {'id': env_var.id, 'name': env_var.name,
                'value': env_var.value,
                'env_id': env_var.env_id,
                'environment': env_var.environment.name}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        value = data['value']
        env_id = data['env_id']
        env_var_obj = EnvVar(name=name, value=value, env_id=env_id)
        response = self.service.add_env_var(env_var_obj)
        if response:
            data['id'] = env_var_obj.id
            return make_response(jsonify(data), 200)

    def put(self, env_var_id):
        env_var_obj = self.service.get_env_var(env_var_id)
        data = request.get_json()
        print(data)
        return self.service.update_env_var(env_var_obj, data)

    def delete(self, env_var_id):
        env_var_obj = self.service.get_env_var(env_var_id)
        return self.service.delete_env_var(env_var_obj)


class EnvVarsController(Resource):
    def __init__(self):
        self.service = EnvVarService()
        # self.model = EnvVar

    def get(self):
        env_vars = self.service.get_all_env_vars()
        resp = {}
        for env_var in env_vars:
            resp[env_var.id] = {'name': env_var.name,
                                'value': env_var.value,
                                'env_id': env_var.env_id,
                                'environment': env_var.environment.name}
        return make_response(jsonify(resp), 200)
