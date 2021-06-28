import datetime

from application.models import user as um
from sqlalchemy import exc
from application import db


class UserService:
    def __init__(self):
        pass

    def get_all_users(self):
        return um.User().query.filter_by(deleted_at=None).all()

    def get_user(self, user_id):
        u = um.User.query.filter_by(id=user_id, deleted_at=None).first()
        if not u:
            raise Exception("User not found")

        return u

    def add_user(self, user_obj):
        try:
            db.session.add(user_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Duplicate user', e)
        else:
            return True

    def update_user(self, user_obj, data):
        for k, v in data.items():
            setattr(user_obj, k, v)

        try:
            db.session.commit()
        except exc.IntegrityError as e:
            raise Exception("Error updating the user", e)
        else:
            return True

    def delete_user(self, user_obj):
        user_obj.deleted_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except:
            raise Exception('Can not deleted user')
