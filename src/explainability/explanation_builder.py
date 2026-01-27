def build_explanation(user, scheme):
    reasons = []

    if user["income"] <= scheme["max_income"]:
        reasons.append("Income is within eligible range")

    if scheme["state"] in ["ALL", user["state"]]:
        reasons.append("Scheme applicable to user's state")

    return reasons
