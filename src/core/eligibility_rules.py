def is_eligible(user_profile, scheme):

    # Income
    income = int(user_profile.get("income", 0))
    max_income = int(scheme.get("max_income", income))
    if income > max_income:
        return False

    # Age
    age = int(user_profile.get("age", 0))
    min_age = int(scheme.get("min_age", 0))
    max_age = int(scheme.get("max_age", 120))
    if not (min_age <= age <= max_age):
        return False

    # State
    s_state = scheme.get("state", "ALL")
    if s_state != "ALL" and s_state != user_profile.get("state"):
        return False

    # Gender
    s_gender = scheme.get("gender", "ALL")
    if s_gender != "ALL" and s_gender != user_profile.get("gender"):
        return False

    # Category
    s_category = scheme.get("category", "ALL")
    if s_category != "ALL" and s_category != user_profile.get("category"):
        return False

    return True
