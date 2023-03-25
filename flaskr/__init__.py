import os

from flask import Flask


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # only during developement, config.py can change that to real secret value (like secrets.token_hex())
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
        UPLOAD_FOLDER=os.path.join(app.instance_path, "uploads"),
        ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
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
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")
    # associates endpoint name "index" with "/" url so thath url_for("index") generates "/"
    # without this only url_for("blog.index") would generate "/" url
    
    from . import contact
    app.register_blueprint(contact.bp)
    app.add_url_rule("/contact", endpoint="contact")

    return app
