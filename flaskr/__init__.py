# run app with flask --app flaskr (--debug) run
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
    
    from . import contact
    app.register_blueprint(contact.bp)
    app.add_url_rule("/contact", endpoint="contact")

    return app

# TODO: 
# A detail view to show a single post. Click a post’s title to go to its page.
# Comments.
# Tags. Clicking a tag shows all the posts with that tag.
# A search box that filters the index page by name.
# Paged display. Only show 5 posts per page.
# Upload an image to go along with a post.
# Format posts using Markdown.
# An RSS feed of new posts.
