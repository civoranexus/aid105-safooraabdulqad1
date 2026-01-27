"""
SchemeAssist AI - Recommendation Engine
This module combines eligibility checking and scoring
to generate ranked scheme recommendations.
"""

from eligibility_check import is_eligible
from scoring import calculate_score

def recommend_schemes(user_profile, schemes):
    """
    Returns a list of recommended schemes sorted by relevance score.
    """
    recommendations = []

    for scheme in schemes:
        if is_eligible(user_profile, scheme):
            score = calculate_score(user_profile, scheme)
            recommendations.append({
                "scheme_name": scheme.get("scheme_name"),
                "score": score,
                "benefits": scheme.get("benefits")
            })
          
    # Sort by score (highest first)
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations
