import os
from flask import Flask, render_template
from . import db,auth

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRETE_KEY='dev',
        DATABASE='flaskr.sqlite' 
    )
    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)
    app.register_blueprint(auth.bp)


    @app.route('/')
    def index():
        return render_template('index.html')

    return app

