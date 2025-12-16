import datetime
from flask import Blueprint, render_template, request, flash
from canvasapi import Canvas

canvas_bp = Blueprint("canvas", __name__, url_prefix="/canvas")


@canvas_bp.route("", methods=["GET", "POST"])
def canvas_page():
    assignments = []

    if request.method == "POST":
        api_url = request.form.get("api_url", "").strip()
        api_key = request.form.get("api_key", "").strip()

        if not api_url or not api_key:
            flash("Please enter both API URL and API key.", "warning")
        else:
            try:
                canvas = Canvas(api_url, api_key)
                now = datetime.datetime.now(datetime.UTC)

                for course in canvas.get_courses():
                    try:
                        # iterate directly here so Forbidden gets caught
                        for a in course.get_assignments():
                            if a.due_at:
                                due_date = datetime.datetime.fromisoformat(
                                    a.due_at.replace("Z", "+00:00")
                                )
                                if due_date > now:
                                    assignments.append(
                                        {
                                            "course_name": course.name,
                                            "assignment_name": a.name,
                                            "due_date": due_date,
                                        }
                                    )
                    except Exception:
                        #Skip class you cant see
                        continue

                assignments.sort(key=lambda x: x["due_date"])

            except Exception:
                flash(
                    "There was an error connecting to Canvas. "
                    "Double-check your API URL and access token.",
                    "danger",
                )

    return render_template("canvas.html", assignments=assignments)
