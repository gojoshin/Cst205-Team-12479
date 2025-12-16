import os
from flask import Flask, render_template
from datetime import timedelta

# Import blueprints
from routes.canvas import canvas_bp
from routes.pomodoro import pomodoro_bp
from routes.spotify import spotify_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")


@app.route("/")
def index():
    # Welcome / user guide page
    return render_template("home.html")

@app.route("/planner")
def planner():
    # Weekly planner page
    return render_template("planner.html")

# Register blueprint routes
app.register_blueprint(canvas_bp)
app.register_blueprint(pomodoro_bp)
app.register_blueprint(spotify_bp)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 5000 for local
    app.run(host="0.0.0.0", port=port, debug=True)
