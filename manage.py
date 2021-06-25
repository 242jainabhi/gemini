# coding: utf-8
import logging

from application import create_app, db, migrate
from flask_restful import Api
from application.controllers.routes import initialize_routes

PORT = 8080
app = create_app()
api = Api(app)

logging.basicConfig(filename='logging/record.log',
                    level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

initialize_routes(api)


@app.route('/')
def run():
    return "Welcome to Gemini"


if __name__ == "__main__":
    app.run(port=5000)
