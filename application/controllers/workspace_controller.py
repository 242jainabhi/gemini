from flask_restful import Resource
from flask import request, make_response, jsonify
from application.models import workspace, user
from application.services import workspace_service as wss, user_service as us
from sqlalchemy import exc
import datetime


class Workspace(Resource):

    def get(self, ws_id):
        w = wss.WorkspaceService().get_workspace(ws_id)
        resp = {'id': w.id, 'name': w.name, 'created_on': w.created_on,
                'creator': [x.name for x in w.users]}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        creator_id = data['creator_id']

        ws_obj = workspace.Workspace(name=name)
        creator = us.UserService().get_user(creator_id)
        # creator = user.User.query.get(creator_id)
        ws_obj.users.append(creator)
        response = wss.WorkspaceService().add_workspace(ws_obj)
        if response:
            data['id'] = ws_obj.id
            return make_response(jsonify(data), 200)

    def put(self, ws_id):
        w = wss.WorkspaceService().get_workspace(ws_id)
        data = request.get_json()
        resp = wss.WorkspaceService().update_workspace(w, data)
        if resp:
            return "Workspace updated successfully"

    def delete(self, ws_id):
        w = wss.WorkspaceService().get_workspace(ws_id)
        w.users = []
        wss.WorkspaceService().delete_workspace(w)
        return f"Deleted workspace with id: {ws_id}"


class Workspaces(Resource):
    def get(self):
        workspaces = wss.WorkspaceService().get_all_workspaces()
        resp = {}
        for w in workspaces:
            resp[w.id] = {'name': w.name, 'created_on': w.created_on,
                          'users': [x.name for x in w.users]}
        return make_response(jsonify(resp), 200)
