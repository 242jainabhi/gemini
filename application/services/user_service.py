import datetime

from application.models.user import User
from sqlalchemy import exc
from application import db


class UserService:
    def __init__(self):
        pass

    def get_all_users(self):
        return User().query.filter_by(deleted_at=None).all()

    def get_user(self, user_id):
        u = User.query.filter_by(id=user_id, deleted_at=None).first()
        if not u:
            raise Exception("User not found")

        return u

    def add_user(self, user_obj):
        # User.query.filter_by(email=user_obj.email, db.isnot(deleted_at, None)).first()
        try:
            db.session.add(user_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('Duplicate user', e)
        else:
            return True

    def update_user(self, user_obj, data):
        if 'name' in data:
            user_obj.name = data['name']
        if 'email' in data:
            user_obj.email = data['email']
        if 'organization' in data:
            user_obj.organization = data['organization']

        # user_obj.updated_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            raise Exception("Error updating the user", e)
        else:
            return "User updated successfully"

    def delete_user(self, user_obj):
        user_obj.deleted_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except:
            raise Exception('Can not deleted user')
        return f"Deleted user with id: {user_obj.id}"