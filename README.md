# 🏋️‍♂️ Fitness Tracker Web App

A Flask-based fitness tracker that helps users monitor their daily calorie intake, calories burned, and remaining calories based on their personal health data.

---

## 🚀 Live Deployment

The latest version of this application is deployed and running live on Railway.

**Access the App Here:** [AI-Powered Fitness Tracker App](https://ai-powered-fitness-calorie-tracker-app-production.up.railway.app)

---

## 📌 Features

- 🔐 Simple login (name, age, height, weight, gender, activity level)
- 🍕 Add food items and track calorie intake
- 🏃 Add burned calories from workouts
- 📊 Displays:
  - Daily required calories
  - Total intake
  - Total burned
  - Remaining calories
- 🔁 Food history list
- ⬇️ Export feature (coming soon)
- 👤 Logout & session tracking

---

## 🖥️ Tech Stack

### 💻 Frontend:
- HTML5, CSS3
- Bootstrap for styling
- JavaScript (vanilla)

### 🧠 Backend:
- Python 3
- Flask (micro web framework)
- Custom calorie prediction module using Mifflin-St Jeor Equation

---

## 🗃️ Project Structure

fitness_tracker_project/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── templates/
│ │ ├── login.html
│ │ └── dashboard.html
│ ├── static/
│ │ ├── css/
│ │ │ └── styles.css
│ │ └── js/ # optional, if using JS
│ └── utils/
│ ├── calorie_predictor.py
│ └── food_database.py
├── run.py
├── requirements.txt
└── README.md