import datetime

from application.models.api_endpoint import ApiEndpoint
from sqlalchemy import exc
from application import db


class ApiEndpointService:
    def __init__(self):
        self.model = ApiEndpoint

    def get_all_api_endpoints(self):
        return self.model.query.filter_by(deleted_at=None).all()

    def get_api_endpoint(self, id):
        endpoint = self.model.query.filter_by(id=id, deleted_at=None).first()
        if not endpoint:
            raise Exception("Api Endpoint not found")

        return endpoint

    def add_api_endpoint(self, api_endpoint_obj):
        try:
            db.session.add(api_endpoint_obj)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            raise Exception('duplicate Api endpoint', e)
        else:
            return True

    def update_api_endpoint(self, api_endpoint_obj, data):
        if 'endpoint' in data:
            api_endpoint_obj.endpoint = data['endpoint']
        if 'method' in data:
            api_endpoint_obj.method = data['method']

        try:
            db.session.commit()
        except exc.IntegrityError as e:
            raise Exception("Error updating the Api Endpoint", e)
        else:
            return "Api endpoint updated successfully"

    def delete_api_endpoint(self, api_endpoint_obj):
        api_endpoint_obj.deleted_at = datetime.datetime.utcnow()
        try:
            db.session.commit()
        except:
            raise Exception('Can not delete api endpoint')
        return f"Deleted api endpoint with id: {api_endpoint_obj.id}"
