from flask import (
    Blueprint, request, render_template, flash, current_app, redirect, url_for
)
from werkzeug.utils import secure_filename
import os
import random
import string

bp = Blueprint("contact", __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

# preliminary, use json.dump() for better accessability/sending around
# or sqlite table for storage on bigger webapps
def save_message(files, path, name, mail, message, mode):
    with open(os.path.join(path, "msg_info"), mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n\n\n")
        f.write(f"Name: {name}\nE-Mail: {mail}\nMessage:\n{message}\n")
    
        if files:
            f.write("Filenames: ")
            for file in files:
                filename = secure_filename(file.filename)
                # random filename if filename empty
                if not filename:
                    filename = ''.join(random.choice(string.ascii_lowercase + string.digits for _ in range(12)))
                # flash but don't abort if unallowed extension
                if not allowed_file(file.filename):
                    flash(f"{filename} has an illicit file extension and was not send")
                f.write(f"{filename}\n")
                file.save(os.path.join(path, filename))


@bp.route("/contact", methods=["POST", "GET"])
def contact():
    """ Makes a directory in the UPLOAD_FOLDER named after the user which contains 
    their E-mail adress, message and uploaded files, if provided. """
    
    if request.method == "POST":
        name = request.form["name"]
        # change name to safe one
        name = "".join([x if x.isalnum() else '_' for x in name])
        if not name:
            flash("Name is required")
            redirect(url_for("contact"))
        mail = request.form["mail"]
        message = request.form["message"]
        files = request.files.getlist("file")

        if not os.path.isdir(current_app.config["UPLOAD_FOLDER"]):
            os.mkdir(current_app.config["UPLOAD_FOLDER"])

        path = os.path.join(current_app.config["UPLOAD_FOLDER"], name)
        try:
            os.mkdir(path)
            save_message(files, path, name, mail, message, "w")

        except FileExistsError:
            save_message(files, path, name, mail, message, "a")

    return render_template("contact.html")
