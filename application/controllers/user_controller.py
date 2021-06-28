from flask import request, make_response, jsonify
from flask_restful import Resource
from application.models import user
from application.services import user_service as us


class User(Resource):

    def get(self, user_id):
        u = us.UserService().get_user(user_id)
        resp = {'id': u.id, 'name': u.name, 'email': u.email,
                'organization': u.organization,
                'workspaces': [x.name for x in u.workspaces]}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        email = data['email']
        organization = data['organization']
        user_obj = user.User(name=name, email=email,
                             organization=organization)
        response = us.UserService().add_user(user_obj)
        if response:
            data['id'] = user_obj.id
            return make_response(jsonify(data), 200)

    def put(self, user_id):
        u = us.UserService().get_user(user_id)
        data = request.get_json()
        resp = us.UserService().update_user(u, data)
        if resp:
            return "User updated successfully"

    def delete(self, user_id):
        u = us.UserService().get_user(user_id)
        us.UserService().delete_user(u)
        return f"Deleted user with id: {user_id}"


class Users(Resource):
    def get(self):
        users = us.UserService().get_all_users()
        resp = {}
        for u in users:
            resp[u.id] = {'name': u.name, 'email': u.email,
                          'organization': u.organization,
                          'workspaces': [x.name for x in u.workspaces]}
            # return u.id, u.name, u.email, u.organization
        return make_response(jsonify(resp), 200)
