# app/utils/food_database.py

indian_foods = [
    # --- MAIN MEALS (NORTH & SOUTH) ---
    {"name": "Roti", "calories": 80, "protein": 3, "carbs": 15, "fats": 0.5},
    {"name": "Butter Roti", "calories": 110, "protein": 3, "carbs": 15, "fats": 3.5},
    {"name": "Paneer", "calories": 265, "protein": 18, "carbs": 1.2, "fats": 20},
    {"name": "Dal Tadka", "calories": 150, "protein": 7, "carbs": 20, "fats": 6},
    {"name": "Dal Makhani", "calories": 250, "protein": 8, "carbs": 22, "fats": 14},
    {"name": "Rice (Boiled)", "calories": 130, "protein": 2.7, "carbs": 28, "fats": 0.3},
    {"name": "Jeera Rice", "calories": 160, "protein": 3, "carbs": 30, "fats": 3},
    {"name": "Chicken Curry", "calories": 240, "protein": 25, "carbs": 8, "fats": 12},
    {"name": "Butter Chicken", "calories": 350, "protein": 22, "carbs": 12, "fats": 24},
    {"name": "Chicken Biryani", "calories": 350, "protein": 18, "carbs": 40, "fats": 12},
    {"name": "Veg Biryani", "calories": 250, "protein": 6, "carbs": 45, "fats": 6},
    {"name": "Dosa (Plain)", "calories": 133, "protein": 2, "carbs": 26, "fats": 3},
    {"name": "Masala Dosa", "calories": 250, "protein": 4, "carbs": 40, "fats": 8},
    {"name": "Idli (2 units)", "calories": 120, "protein": 4, "carbs": 24, "fats": 0.2},
    {"name": "Sambhar", "calories": 80, "protein": 3, "carbs": 12, "fats": 2},
    {"name": "Vada (1 unit)", "calories": 110, "protein": 2, "carbs": 15, "fats": 5},
    {"name": "Chole", "calories": 210, "protein": 8, "carbs": 30, "fats": 6},
    {"name": "Bhature (1 unit)", "calories": 220, "protein": 4, "carbs": 28, "fats": 10},
    {"name": "Aloo Paratha", "calories": 210, "protein": 4, "carbs": 35, "fats": 7},
    {"name": "Paneer Paratha", "calories": 280, "protein": 12, "carbs": 30, "fats": 12},
    {"name": "Rajma Chawal", "calories": 320, "protein": 12, "carbs": 55, "fats": 5},
    {"name": "Kadai Paneer", "calories": 280, "protein": 15, "carbs": 10, "fats": 18},
    {"name": "Palak Paneer", "calories": 240, "protein": 14, "carbs": 10, "fats": 16},
    {"name": "Mix Veg", "calories": 150, "protein": 4, "carbs": 18, "fats": 7},
    {"name": "Matar Paneer", "calories": 260, "protein": 13, "carbs": 12, "fats": 18},
    {"name": "Egg Bhurji", "calories": 180, "protein": 14, "carbs": 4, "fats": 12},
    {"name": "Chicken Tikka", "calories": 220, "protein": 30, "carbs": 4, "fats": 10},

    # --- MAHARASHTRIAN & GUJARATI ---
    {"name": "Poha", "calories": 180, "protein": 3, "carbs": 35, "fats": 3},
    {"name": "Misal Pav", "calories": 400, "protein": 12, "carbs": 50, "fats": 18},
    {"name": "Vada Pav", "calories": 280, "protein": 5, "carbs": 40, "fats": 11},
    {"name": "Pav Bhaji", "calories": 450, "protein": 9, "carbs": 60, "fats": 20},
    {"name": "Sabudana Khichdi", "calories": 320, "protein": 3, "carbs": 65, "fats": 6},
    {"name": "Dhokla (3 units)", "calories": 160, "protein": 6, "carbs": 24, "fats": 4},
    {"name": "Thepla (1 unit)", "calories": 100, "protein": 3, "carbs": 16, "fats": 3},
    {"name": "Khandvi", "calories": 120, "protein": 4, "carbs": 15, "fats": 5},
    {"name": "Kanda Bhaji", "calories": 200, "protein": 3, "carbs": 25, "fats": 10},
    {"name": "Zunka Bhakri", "calories": 350, "protein": 10, "carbs": 50, "fats": 12},
    {"name": "Puran Poli", "calories": 300, "protein": 6, "carbs": 55, "fats": 7},

    # --- SNACKS & FAST FOOD ---
    {"name": "Samosa (1 unit)", "calories": 250, "protein": 4, "carbs": 25, "fats": 15},
    {"name": "Bread Pakora", "calories": 280, "protein": 6, "carbs": 30, "fats": 16},
    {"name": "Maggi (1 pack)", "calories": 310, "protein": 7, "carbs": 45, "fats": 12},
    {"name": "Pani Puri (6 units)", "calories": 180, "protein": 3, "carbs": 35, "fats": 4},
    {"name": "Bhel Puri", "calories": 210, "protein": 4, "carbs": 38, "fats": 5},
    {"name": "Aloo Tikki", "calories": 180, "protein": 3, "carbs": 25, "fats": 8},
    {"name": "Momos Veg (5 units)", "calories": 175, "protein": 5, "carbs": 35, "fats": 2},
    {"name": "Momos Chicken (5 units)", "calories": 250, "protein": 15, "carbs": 35, "fats": 6},
    {"name": "Spring Roll", "calories": 150, "protein": 3, "carbs": 20, "fats": 7},
    {"name": "Oats", "calories": 160, "protein": 6, "carbs": 28, "fats": 3},
    {"name": "Peanuts (Roasted, 30g)", "calories": 170, "protein": 7, "carbs": 5, "fats": 14},

    # --- FRUITS & DAIRY ---
    {"name": "Egg (Boiled)", "calories": 78, "protein": 6, "carbs": 0.6, "fats": 5},
    {"name": "Milk (1 cup)", "calories": 120, "protein": 7, "carbs": 10, "fats": 5},
    {"name": "Curd (1 cup)", "calories": 100, "protein": 6, "carbs": 8, "fats": 4},
    {"name": "Buttermilk", "calories": 40, "protein": 2, "carbs": 5, "fats": 1},
    {"name": "Paneer (Raw 100g)", "calories": 265, "protein": 18, "carbs": 2, "fats": 20},
    {"name": "Apple", "calories": 52, "protein": 0.3, "carbs": 14, "fats": 0.2},
    {"name": "Banana", "calories": 90, "protein": 1.1, "carbs": 23, "fats": 0.3},
    {"name": "Mango", "calories": 150, "protein": 1.5, "carbs": 35, "fats": 0.5},
    {"name": "Orange", "calories": 50, "protein": 1, "carbs": 12, "fats": 0.2},
    {"name": "Papaya (1 cup)", "calories": 60, "protein": 0.6, "carbs": 15, "fats": 0.1},

    # --- SWEETS & BEVERAGES ---
    {"name": "Gulab Jamun (1 unit)", "calories": 150, "protein": 2, "carbs": 25, "fats": 5},
    {"name": "Jalebi (2 units)", "calories": 100, "protein": 0.5, "carbs": 20, "fats": 3},
    {"name": "Tea (with Milk/Sugar)", "calories": 60, "protein": 1, "carbs": 10, "fats": 2},
    {"name": "Coffee (with Milk/Sugar)", "calories": 80, "protein": 2, "carbs": 12, "fats": 3},
    {"name": "Green Tea", "calories": 2, "protein": 0, "carbs": 0.5, "fats": 0},
    {"name": "Protein Shake", "calories": 150, "protein": 25, "carbs": 5, "fats": 2},
]

# Case-insensitive lookup dictionary
FOOD_DATA = {item["name"].lower(): item for item in indian_foods}