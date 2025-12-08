from flask import Blueprint, render_template

canvas_bp = Blueprint("canvas", __name__)

@canvas_bp.route("/canvas")
def canvas_page():
    return render_template("canvas.html")
