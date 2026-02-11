def is_eligible(user_profile, scheme):
    # 1. Income Check
    income = int(user_profile.get("income", 0))
    max_income = int(scheme.get("max_income", income))
    if income > max_income: return False

    # 2. Age Check
    age = int(user_profile.get("age", 0))
    min_age = int(scheme.get("min_age", 0))
    max_age = int(scheme.get("max_age", 100))
    if not (min_age <= age <= max_age): return False

    # 3. State Check (Handles 'ALL' for central schemes)
    s_state = scheme.get("state", "ALL")
    if s_state != "ALL" and s_state != user_profile.get("state"):
        return False

    # 4. Gender Check
    s_gender = scheme.get("gender", "ALL")
    if s_gender != "ALL" and s_gender != user_profile.get("gender"):
        return False

    return True