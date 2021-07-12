from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models.user import User
from application.services.user_service import UserService


class UserController(Resource):
    def __init__(self):
        self.service = UserService()

    def get(self, user_id):
        u = self.service.get_user(user_id)
        resp = {'id': u.id, 'name': u.name, 'email': u.email,
                'organization': u.organization,
                'workspaces': [x.name for x in u.workspaces]}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        email = data['email']
        organization = data['organization']
        user_obj = User(name=name, email=email, organization=organization)
        response = self.service.add_user(user_obj)
        if response:
            data['id'] = user_obj.id
            return make_response(jsonify(data), 200)

    def put(self, user_id):
        u = self.service.get_user(user_id)
        data = request.get_json()
        return self.service.update_user(u, data)

    def delete(self, user_id):
        # delete user and relation
        u = self.service.get_user(user_id)
        return self.service.delete_user(u)


class Users(Resource):
    def __init__(self):
        self.service = UserService()

    def get(self):
        users = self.service.get_all_users()
        resp = {}
        for u in users:
            resp[u.id] = {'name': u.name, 'email': u.email,
                          'organization': u.organization,
                          'workspaces': [x.name for x in u.workspaces]}
            # return u.id, u.name, u.email, u.organization
        return make_response(jsonify(resp), 200)
