def check_basic_eligibility(user, scheme):
    if user["income"] > scheme["max_income"]:
        return False

    if scheme["state"] not in ["ALL", user["state"]]:
        return False

    return True
