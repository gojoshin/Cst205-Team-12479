import express from "express";
import fetch from "node-fetch";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

dotenv.config();

// Create Express app
const app = express();

// Fix __dirname in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Set EJS as the templating engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// --- MOCK API DATA FUNCTION ---
async function fetchTweekPlannerData(authToken) {
  // MOCK DATA for demonstration purpose
  return [
    { id: 1, date: "2025-12-15", day: "Monday", task: "Review Express.js implementation", status: "Completed", color: "green" },
    { id: 2, date: "2025-12-16", day: "Tuesday", task: "Plan Tweek API integration strategy", status: "In Progress", color: "blue" },
    { id: 3, date: "2025-12-17", day: "Wednesday", task: "Write documentation for new feature", status: "Pending", color: "yellow" },
    { id: 4, date: "2025-12-18", day: "Thursday", task: "Team Meeting (10:00 AM)", status: "Pending", color: "blue" },
    { id: 5, date: "2025-12-19", day: "Friday", task: "Push weekly summary to GitHub", status: "Pending", color: "yellow" }
  ];
}

// Route for planner
app.get("/planner", async (req, res) => {
  const MOCK_AUTH_TOKEN = "YOUR_SECURE_JWT_TOKEN_HERE";
  const plannerData = await fetchTweekPlannerData(MOCK_AUTH_TOKEN);
  res.render("planner", {
    title: "Tweek Planner Table",
    tasks: plannerData
  });
});

// Route for home
app.get("/", (req, res) => {
  res.render("home");
});

// Serve static files
app.use(express.static("public"));

// Start server
app.listen(3000, () => console.log("Server running at http://localhost:3000"));
