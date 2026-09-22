import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRETE_KEY='dev',
        DATABASE='flaskr.sqlite' 
    )
    print(app.instance_path)
    os.makedirs(app.instance_path, exist_ok=True)

    @app.route('/')
    def hello():
        app.debug=True
        return 'Hello World!

    return app

