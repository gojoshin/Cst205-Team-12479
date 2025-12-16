import express from "express";
import fetch from "node-fetch";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

dotenv.config();

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// --- MOCK Tweek API DATA FUNCTION ---
async function fetchTweekPlannerData(authToken) {
  // Replace with real Tweek API call if available
  return [
    { id: 1, date: "2025-12-15", day: "Monday", task: "Review Express.js implementation", status: "Completed", color: "green" },
    { id: 2, date: "2025-12-16", day: "Tuesday", task: "Plan Tweek API integration strategy", status: "In Progress", color: "blue" },
    { id: 3, date: "2025-12-17", day: "Wednesday", task: "Write documentation for new feature", status: "Pending", color: "yellow" },
    { id: 4, date: "2025-12-18", day: "Thursday", task: "Team Meeting (10:00 AM)", status: "Pending", color: "blue" },
    { id: 5, date: "2025-12-19", day: "Friday", task: "Push weekly summary to GitHub", status: "Pending", color: "yellow" }
  ];
}
async function fetchCanvasAssignments(apiUrl, apiKey) {
  const assignments = [];
  try {
    const coursesRes = await fetch(`${apiUrl}/api/v1/courses`, {
      headers: { Authorization: `Bearer ${apiKey}` }
    });
    const courses = await coursesRes.json();
    const now = new Date();

    for (const course of courses) {
      try {
        const assignmentsRes = await fetch(`${apiUrl}/api/v1/courses/${course.id}/assignments`, {
          headers: { Authorization: `Bearer ${apiKey}` }
        });
        const courseAssignments = await assignmentsRes.json();

        for (const a of courseAssignments) {
          if (a.due_at) {
            const dueDate = new Date(a.due_at);
            if (dueDate > now) {
              assignments.push({
                course_name: course.name,
                assignment_name: a.name,
                due_date: dueDate
              });
            }
          }
        }
      } catch {
        continue; 
      }
    }
    assignments.sort((a, b) => a.due_date - b.due_date);
  } catch (err) {
    console.error("Canvas API error:", err);
  }
  return assignments;
}


// Home route
app.get("/", (req, res) => {
  res.render("home");
});

// Tweek planner route
app.get("/planner", async (req, res) => {
  const MOCK_AUTH_TOKEN = "YOUR_SECURE_JWT_TOKEN_HERE";
  const plannerData = await fetchTweekPlannerData(MOCK_AUTH_TOKEN);
  res.render("planner", {
    title: "Tweek Planner Table",
    tasks: plannerData
  });
});

// Canvas planner route 
app.get("/canvas", (req, res) => {
  res.render("canvas", { assignments: [], message: null });
});

app.post("/canvas", async (req, res) => {
  const apiUrl = (req.body.api_url || "").trim();
  const apiKey = (req.body.api_key || "").trim();
  if (!apiUrl || !apiKey) {
    return res.render("canvas", { assignments: [], message: "Please enter both API URL and API key." });
  }
  const assignments = await fetchCanvasAssignments(apiUrl, apiKey);
  res.render("canvas", { assignments, message: null });
});

app.use(express.static("public"));
app.listen(3000, () => console.log("Server running at http://localhost:3000"));
