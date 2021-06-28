import datetime

from application.models import workspace as wsm
from sqlalchemy import exc
from application import db


class WorkspaceService:
    def __init__(self):
        pass

    def get_all_workspaces(self):
        return wsm.Workspace.query.filter_by(deleted_at=None).all()

    def get_workspace(self, ws_id):
        ws = wsm.Workspace.query.filter_by(id=ws_id, deleted_at=None).first()
        if not ws:
            raise Exception("Workspace not found")

        return ws

    def add_workspace(self, ws_obj):
        try:
            db.session.add(ws_obj)
            # create association here by calling association service
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Duplicate workspace', e)
        else:
            return True

    def update_workspace(self, ws_obj, data):
        for k, v in data.items():
            setattr(ws_obj, k, v)

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
