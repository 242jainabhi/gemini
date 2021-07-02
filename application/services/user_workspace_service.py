from application import db
import sys


class UserWSService:
    def add_association(self, u_ws_obj):
        try:
            db.session.add(u_ws_obj)
            db.session.commit()
        except:
            db.session.rollback()
            return (False, sys.exc_info()[1]._message)
        return (True, 'Successful')

    def delete_association(self):
        pass
