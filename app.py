import os
from flask import Flask, render_template

# Import blueprints
from routes.canvas import canvas_bp
from routes.pomodoro import pomodoro_bp
from routes.spotify import spotify_bp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

# Register blueprint routes
app.register_blueprint(canvas_bp)
app.register_blueprint(pomodoro_bp)
app.register_blueprint(spotify_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 5000 for local
    app.run(host="0.0.0.0", port=port)
