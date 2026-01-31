def compute_score(user, scheme):
    score = 0

    if user["state"] == scheme["state"]:
        score += 30

    score += scheme["priority_weight"]
    return score
