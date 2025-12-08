import datetime
from canvasapi import Canvas

API_URL = "https://csumb.instructure.com"
API_KEY = "2263~cakk68ZK4rkTYJ2xAhR9h4YfR2VDX66EWymkCrBmQ9T22aBNaeQ4urLLJwKAB9M3"

canvas = Canvas(API_URL, API_KEY)

now = datetime.datetime.now(datetime.UTC)

print("Upcoming Assignments:\n")

for course in canvas.get_courses():
    try:
        assignments = course.get_assignments()
    except Exception:
        continue  # some courses aren't accessible

    for a in assignments:
        if a.due_at:
            due_date = datetime.datetime.fromisoformat(a.due_at.replace("Z", "+00:00"))
            if due_date > now:
                print(f"{course.name} → {a.name} due on {due_date}")
