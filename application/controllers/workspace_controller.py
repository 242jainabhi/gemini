from flask_restful import Resource
from flask import request, make_response, jsonify
from application.models.workspace import Workspace
from application.services.workspace_service import WorkspaceService
from application.services.user_service import UserService
from sqlalchemy import exc
import datetime


class WorkspaceController(Resource):
    def __init__(self):
        self.service = WorkspaceService()
        self.user_service = UserService()

    def get(self, ws_id):
        w = self.service.get_workspace(ws_id)
        resp = {'id': w.id, 'name': w.name, 'created_at': w.created_at,
                'users': [x.name for x in w.users]}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        creator_id = data['creator_id']

        # check if user exists. if not, user_service wil raise exception
        u = self.user_service.get_user(creator_id)

        ws_obj = Workspace(name=name)
        response = self.service.add_workspace(ws_obj, u.id)
        if response:
            data['id'] = ws_obj.id
            return make_response(jsonify(data), 200)

    def put(self, ws_id):
        w = self.service.get_workspace(ws_id)
        data = request.get_json()
        resp = self.service.update_workspace(w, data)
        if resp:
            return "Workspace updated successfully"

    def delete(self, ws_id):
        # delete workspace and relation
        w = self.service.get_workspace(ws_id)

        w.users = []
        self.service.delete_workspace(w)
        return f"Deleted workspace with id: {ws_id}"


class Workspaces(Resource):
    def __init__(self):
        self.service = WorkspaceService()

    def get(self):
        workspaces = self.service.get_all_workspaces()
        resp = {}
        for w in workspaces:
            resp[w.id] = {'name': w.name, 'created_at': w.created_at,
                          'users': [x.name for x in w.users]}
        return make_response(jsonify(resp), 200)
