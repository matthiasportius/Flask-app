# run app with flask --app flaskr (--debug) run
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # only during developement, config.py can change that to real secret value
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # load instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load test config is passed in
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World"
    
    # db can now be initialized with "flask --app flaskr init-db" 
    from . import db
    db.init_app(app)

    return app
