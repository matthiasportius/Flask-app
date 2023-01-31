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
        return "Hello, World!"
    
    # initialize db with "flask --app flaskr init-db" 
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")
    # associates endpoint name "index" with "/" url so thath url_for("index") works and generates "/"
    # without this only url_for("blog.index") would work
    # app.route("/") def index would do the same
    # could also give blog Blueprint a url_prefix like auth and define seperate index view in the application factory (__init__)
    # then the index in __init__ and the blog.index (with url_prefix) would be different
    
    return app
