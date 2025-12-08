from flask import Blueprint, render_template

spotify_bp = Blueprint("spotify", __name__)

@spotify_bp.route("/spotify")
def spotify_page():
    return render_template("spotify.html")
