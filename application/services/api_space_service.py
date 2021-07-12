import datetime

from application.models.api_space import ApiSpace
from sqlalchemy import exc
from application import db


class ApiSpaceService:
    def __init__(self):
        self.model = ApiSpace

    def get_all_api_spaces(self):
        return self.model.query.filter_by(deleted_at=None).all()

    def get_api_space(self, id):
        space = self.model.query.filter_by(id=id, deleted_at=None).first()
        if not space:
            raise Exception("Api Space not found")

        return space

    def add_api_space(self, api_space_obj):
        # User.query.filter_by(email=user_obj.email, db.isnot(deleted_at, None)).first()
        try:
            db.session.add(api_space_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('duplicate Api Space', e)
        else:
            return True

    def update_api_space(self, api_space_obj, data):
        if 'name' in data:
            api_space_obj.name = data['name']
        if 'documentation' in data:
            api_space_obj.documentation = data['documentation']

        try:
            db.session.commit()
        except exc.IntegrityError as e:
            raise Exception("Error updating the Api Space", e)
        else:
            return "Api Space updated successfully"

    def delete_api_space(self, api_space_obj):
        api_space_obj.deleted_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except:
            raise Exception('Can not delete api space')
        return f"Deleted api space with id: {api_space_obj.id}"
