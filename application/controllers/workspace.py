from flask_restful import Resource
from flask import request, make_response, jsonify
from application.models import workspace, user
from application import db
from sqlalchemy import exc
import datetime
# from flask import current_app as app


class Workspace(Resource):
    def get(self, id):
        w = workspace.Workspace.query.filter_by(id=id, deleted_at=None).first()
        if not w:
            return "Workspace not found"
        resp = {'id': w.id, 'name': w.name, 'created_on': w.created_on, 'creator': w.users[0].name}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        creator_id = data['creator_id']

        ws_obj = workspace.Workspace(name=name)
        creator = user.User.query.get(creator_id)
        ws_obj.users.append(creator)
        try:
            db.session.add(ws_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            # return e.args
            return "Constraint Violated"
        else:
            data['id'] = ws_obj.id
            return make_response(jsonify(data), 200)

    def put(self, id):
        data = request.get_json()
        w = workspace.Workspace.query.get(id)
        if 'name' in data:
            w.name = data['name']

        try:
            db.session.commit()
        except:
            return "Workspace could not be updated"
        else:
            return "Workspace updated successfully"

    def delete(self, id):
        w = workspace.Workspace.query.get(id)
        if w:
            w.deleted_at = datetime.datetime.utcnow()
            db.session.commit()
        else:
            return make_response("Workspace Not found", 404)
        return f"Deleted workspace with id: {id}"


class Workspaces(Resource):
    def get(self):
        workspaces = workspace.Workspace.query.all()
        resp = {}
        for w in workspaces:
            resp[w.id] = {'name': w.name, 'created_on': w.created_on,  'users': [x.name for x in w.users]}
        return make_response(jsonify(resp), 200)
