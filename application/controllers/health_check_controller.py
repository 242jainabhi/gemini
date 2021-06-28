from flask_restful import Resource
from flask import current_app as app


class Health(Resource):
    def get(self):
        app.logger.info('Info level log')
        app.logger.warning('Warning level log')
        return True
