def calculate_required_calories(gender, age, weight, height, activity_level):
    """
    Returns daily required calories using the Mifflin-St Jeor Equation.
    weight: in kg
    height: in cm
    age: in years
    """

    # Basal Metabolic Rate (BMR) formula
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age  # fallback, no gender adjustment

    # Activity multiplier
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }

    multiplier = activity_multipliers.get(activity_level.lower(), 1.2)
    return round(bmr * multiplier)
