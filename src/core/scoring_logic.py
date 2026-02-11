def compute_score(user, scheme):
    score = 0

    # Income closeness (lower gap = higher score)
    income_gap = scheme["max_income"] - user["income"]
    if income_gap >= 0:
        score += max(0, 30 - (income_gap // 10000))

    # State relevance
    if scheme["state"] == user["state"]:
        score += 20

    # Category relevance
    if scheme["category"] == user["category"]:
        score += 25

    # Scheme priority
    score += scheme["priority_weight"] * 5

    return score
