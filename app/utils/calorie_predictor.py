def calculate_required_calories(gender, age, weight, height, activity_level):
    """
    Returns TDEE (Total Daily Energy Expenditure)
    using the Mifflin-St Jeor Equation.
    """
    # 🧪 Step 1: Calculate BMR (Basal Metabolic Rate)
    if gender.lower() == 'male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # 🏃 Step 2: Apply Activity Multiplier
    # Mapping must align with your login.html dropdown values
    activity_multipliers = {
        'sedentary': 1.2,  # Little or no exercise
        'lightly active': 1.375,  # Light exercise 1-3 days/week
        'moderately active': 1.55,  # Moderate exercise 3-5 days/week
        'very active': 1.725,  # Hard exercise 6-7 days/week
        'extra active': 1.9  # Very hard exercise & physical job
    }

    # Default to sedentary if level is not identified
    multiplier = activity_multipliers.get(activity_level.lower(), 1.2)

    return round(bmr * multiplier)


def get_bmi_status(weight, height):
    """Calculates BMI and returns status with a theme color for UI."""
    # Formula: weight (kg) / [height (m)]^2
    bmi = round(weight / ((height / 100) ** 2), 1)

    if bmi < 18.5:
        return bmi, "Underweight", "#ff4d4d"  # Red
    elif bmi < 25:
        return bmi, "Healthy", "#00f2ff"  # Cyan/Neon
    elif bmi < 30:
        return bmi, "Overweight", "#ffcc00"  # Yellow
    else:
        return bmi, "Obese", "#ff4444"  # Deep Red