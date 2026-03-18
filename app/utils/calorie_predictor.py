def calculate_required_calories(gender, age, weight, height, activity_level):
    """Returns daily required calories using the Mifflin-St Jeor Equation."""
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }

    multiplier = activity_multipliers.get(activity_level.lower(), 1.2)
    return round(bmr * multiplier)

def get_bmi_status(weight, height):
    """Calculates BMI and returns status with a theme color."""
    bmi = round(weight / ((height / 100) ** 2), 1)
    if bmi < 18.5:
        return bmi, "Underweight", "#ff4d4d"
    elif bmi < 25:
        return bmi, "Healthy", "#00f2ff"
    elif bmi < 30:
        return bmi, "Overweight", "#ffcc00"
    else:
        return bmi, "Obese", "#ff4444"