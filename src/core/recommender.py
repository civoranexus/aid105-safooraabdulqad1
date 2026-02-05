from core.eligibility_rules import check_basic_eligibility
from core.scoring_logic import compute_score
from explainability.explanation_builder import build_explanation
from explainability.rejection_reasons import build_rejection_reasons

def recommend_schemes(user_profile, schemes):
    """
    Generate ranked scheme recommendations with explanations.
    """
    recommendations = []

    for scheme in schemes:
        if check_basic_eligibility(user_profile, scheme):
            score = compute_score(user_profile, scheme)
            reasons = build_explanation(user_profile, scheme)

            recommendations.append({
                "scheme_name": scheme.get("scheme_name"),
                "score": score,
                "reasons": reasons
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations
