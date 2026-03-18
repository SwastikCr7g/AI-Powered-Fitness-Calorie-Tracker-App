# ⚡ Fitness Pro: AI-Powered Bio-Metric Tracker

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-white?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-green?style=for-the-badge&logo=sqlite)

Nexus Fitness Pro is a high-performance, persistent fitness ecosystem designed to provide deep insights into your daily health. Beyond simple calorie tracking, it uses **AI-driven heuristics** to analyze your BMI and suggest real-time nutritional adjustments.

---

## 🚀 Live Deployment
The latest version of this application is deployed on **Railway**.
🔗 **[Access Nexus Pro Here](https://ai-powered-fitness-calorie-tracker-app-production.up.railway.app)**

---

## 📌 Pro Features (v2.0 Updates)

- 📊 **Dynamic Macro Dashboard**: Real-time visualization of Protein, Carbs, and Fats using **Chart.js** doughnuts.
- 💾 **Persistent Data Sync**: Integrated **SQLAlchemy ORM** with SQLite to ensure your logs and profile never reset.
- 📉 **Bio-Status Analyzer**: Automatically calculates **BMI** and provides a color-coded health status (Healthy/Overweight/Obese).
- 🥗 **AI Meal Suggester**: Evaluates remaining calorie capacity and recommends specific Indian meals from the database.
- 💧 **Hydration Tracker**: Dedicated water intake logging system with animated glass counters.
- 📂 **Smart Export**: Generate a full JSON-based bio-metric report including macro-breakdowns and historical logs.
- 🔍 **Datalist Search**: Intuitive "Search-as-you-type" interface for a database of 1000+ validated Indian food items.

---

## 🖥️ Next-Gen Tech Stack

### **Frontend:**
- **UI/UX**: Glassmorphic Cyber-Dark Theme (CSS3 + Poppins/Orbitron Fonts).
- **Visualization**: Chart.js for real-time macro-nutrient distribution.
- **Icons**: FontAwesome 6.0 integration.

### **Backend:**
- **Engine**: Python 3.12 / Flask (Micro-framework).
- **Logic**: Mifflin-St Jeor BMR Equation & BMI Heuristics.
- **Database**: SQLite with SQLAlchemy (Persistent User Models).

---

## 🗃️ Project Structure

```text
fitness_tracker_project/
├── app/
│   ├── main.py             # Central Entry Point & Filters
│   ├── routes.py           # AI Logic & API Endpoints
│   ├── models.py           # Database Schema (Users/Stats)
│   ├── templates/          # Next-Gen Glassmorphic UI
│   ├── static/             # Assets & Cyber-Theme CSS
│   └── utils/
│       ├── calorie_predictor.py  # BMR & BMI Algorithms
│       └── food_database.py      # 1000+ Macro-Nutrient Dataset
├── run.py                  # Dev Server Script
└── requirements.txt        # Production Dependencies
🛠️ Installation & Setup
Clone & Enter:

Bash
git clone [https://github.com/SwastikCr7g/AI-Powered-Fitness-Calorie-Tracker-App.git](https://github.com/SwastikCr7g/AI-Powered-Fitness-Calorie-Tracker-App.git)
cd AI-Powered-Fitness-Calorie-Tracker-App
Install Pro Dependencies:

Bash
pip install -r requirements.txt
Initialize System:

Bash
python main.py
Developed with ❤️ by Swastik Gahukar