from flask_restful import Resource
from flask import request, make_response, jsonify
from application.models import user
from application import db
from sqlalchemy import exc
import datetime
# from flask import current_app as app


class User(Resource):

    def get(self, id):
        u = user.User.query.filter_by(id=id, deleted_at=None).first()
        if not u:
            return "User not found"
        resp = {'id': u.id, 'name': u.name, 'email': u.email, 'organization': u.organization, 'workspaces': [x.name for x in u.workspaces]}
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        email = data['email']
        organization = data['organization']
        user_obj = user.User(name=name, email=email, organization=organization)
        try:
            db.session.add(user_obj)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return "Duplicate Email"
        else:
            data['id'] = user_obj.id
            return make_response(jsonify(data), 200)

    def put(self, id):
        data = request.get_json()
        u = user.User.query.get(id)
        if 'name' in data:
            u.name = data['name']
        if 'email' in data:
            u.email = data['email']
        if 'organization' in data:
            u.organization = data['organization']

        try:
            db.session.commit()
        except:
            return "User could not be updated"
        else:
            return "User updated successfully"

    def delete(self, id):
        # u = user.User.query.get_or_404(id)
        u = user.User.query.get(id)
        if u:
            u.deleted_at = datetime.datetime.utcnow()
            db.session.commit()
        else:
            return make_response("User Not found", 404)
        return f"Deleted user with id: {id}"


class Users(Resource):
    def get(self):
        users = user.User.query.all()
        resp = {}
        for u in users:
            resp[u.id] = {'name': u.name, 'email': u.email, 'organization': u.organization,  'workspaces': [x.name for x in u.workspaces]}
            # return u.id, u.name, u.email, u.organization
        return make_response(jsonify(resp), 200)
