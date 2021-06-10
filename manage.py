# coding: utf-8
from application import create_app
from flask_restful import Api
import logging
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
    app.run(host='0.0.0.0', port=8080)
