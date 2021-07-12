import datetime

from application.models.env_var import EnvVar
from sqlalchemy import exc
from application import db


class EnvVarService:
    def __init__(self):
        self.model = EnvVar

    def get_all_env_vars(self):
        return self.model.query.filter_by(deleted_at=None).all()

    def get_env_var(self, id):
        env_var = self.model.query.filter_by(id=id, deleted_at=None).first()
        if not env_var:
            raise Exception("Environment variable not found")

        return env_var

    def add_env_var(self, env_var_obj):
        # User.query.filter_by(email=user_obj.email, db.isnot(deleted_at, None)).first()
        try:
            db.session.add(env_var_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Duplicate Environment variable', e)
        else:
            return True

    def update_env_var(self, env_var_obj, data):
        if 'name' in data:
            env_var_obj.name = data['name']

        try:
            db.session.commit()
        except exc.IntegrityError as e:
            raise Exception("Error updating the Environment variable", e)
        else:
            return "Environment variable updated successfully"

    def delete_env_var(self, env_var_obj):
        env_var_obj.deleted_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except:
            raise Exception('Can not delete environment variable')
        return f"Deleted environment variable with id: {env_var_obj.id}"
