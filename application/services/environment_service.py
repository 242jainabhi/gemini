import datetime

from application.models.environment import Environment
from sqlalchemy import exc
from application import db


class EnvironmentService:
    def __init__(self):
        self.model = Environment

    def get_all_envs(self):
        return self.model.query.filter_by(deleted_at=None).all()

    def get_environment(self, id):
        env = self.model.query.filter_by(id=id, deleted_at=None).first()
        if not env:
            raise Exception("Environment not found")

        return env

    def add_environment(self, env_obj):
        # User.query.filter_by(email=user_obj.email, db.isnot(deleted_at, None)).first()
        try:
            db.session.add(env_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Duplicate Environment', e)
        else:
            return True

    def update_environment(self, env_obj, data):
        if 'name' in data:
            env_obj.name = data['name']

        try:
            db.session.commit()
        except exc.IntegrityError as e:
            raise Exception("Error updating the Environment", e)
        else:
            return "Environment updated successfully"

    def delete_environment(self, env_obj):
        env_obj.deleted_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except:
            raise Exception('Can not delete environment')
        return f"Deleted environment with id: {env_obj.id}"
