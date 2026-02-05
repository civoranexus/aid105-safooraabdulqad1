def check_basic_eligibility(user, scheme):
    if user["income"] > scheme["max_income"]:
        return False

    if scheme["state"] not in ["ALL", user["state"]]:
        return False

    if scheme["category"] not in ["General", user["category"]]:
        return False

    return True

