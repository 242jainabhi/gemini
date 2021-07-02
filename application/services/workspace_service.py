import datetime

from application.constants import RoleEnum
from application.models.workspace import Workspace
from application.models.user_workspace import UserWorkspace
from application.services.user_service import UserService
from application.services.user_workspace_service import UserWSService
from sqlalchemy import exc
from application import db


class WorkspaceService:
    def __init__(self):
        pass

    def get_all_workspaces(self):
        return Workspace.query.filter_by(deleted_at=None).all()

    def get_workspace(self, ws_id):
        ws = Workspace.query.filter_by(id=ws_id, deleted_at=None).first()
        if not ws:
            raise Exception("Workspace not found")

        return ws

    def add_workspace(self, ws_obj, creator_id):
        try:
            db.session.add(ws_obj)
            db.session.commit()

            # add association, then add workspace
            u_ws_obj = UserWorkspace(user_id=creator_id, workspace_id=ws_obj.id,
                                     role=RoleEnum.ADMIN)
            resp = UserWSService().add_association(u_ws_obj)
            if not resp[0]:
                db.session.delete(ws_obj)
                db.session.commit()
                raise Exception(resp[1])

        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Duplicate workspace', e)
        else:
            return True

    def update_workspace(self, ws_obj, data):
        if 'name' in data:
            ws_obj.name = data['name']
        # ws_obj.updated_at = datetime.datetime.utcnow()

        try:
            db.session.commit()
        except exc.IntegrityError as e:
            raise Exception("Error updating the workspace", e)
        else:
            return True

    def delete_workspace(self, ws_obj):
        ws_obj.deleted_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except:
            raise Exception('Can not deleted workspace')
