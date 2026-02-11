"""
SchemeAssist AI - Eligibility Scoring Module
This module assigns a relevance score to an eligible scheme
based on how well it matches the user profile.
"""

def calculate_score(user_profile, scheme):
    """
    Returns a score representing how relevant a scheme is
    for the given user profile.
    """
    score = 0
  
    # Income relevance
    score += 40

    # State relevance
    if scheme.get("state") in ["ALL", user_profile["state"]]:
        score += 30

    # Category relevance
    if scheme.get("category") in ["ALL", user_profile["category"]]:
        score += 30

    return score
