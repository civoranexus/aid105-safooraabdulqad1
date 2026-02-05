def build_rejection_reasons(user, scheme):
    reasons = []

    if user["income"] > scheme["max_income"]:
        reasons.append("Income exceeds scheme limit")

    if scheme["state"] not in ["ALL", user["state"]]:
        reasons.append("Scheme not applicable in user's state")

    if scheme["category"] != user["category"]:
        reasons.append("User category does not match scheme")

    return reasons
