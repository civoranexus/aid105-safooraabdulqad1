from src.core.eligibility_rules import is_eligible
from src.explainability.explanation_builder import build_explanation
from src.core.scoring_logic import compute_score

def recommend_schemes(user_profile, schemes):
    recommendations = []
    for scheme in schemes:
        # Evaluates based on core factors: Age, Income, State, Category, Gender
        if is_eligible(user_profile, scheme): 
            score = compute_score(user_profile, scheme)
            
            # Generates the 'AI Reasoning' list for the UI
            reasons = build_explanation(user_profile, scheme) 
            
            recommendations.append({
                "scheme_name": scheme.get("scheme_name"),
                "score": score,
                "benefit": scheme.get("benefit"), # Key synced with schemes.csv
                "reasons": reasons
            })
    
    # Sorts by score to show the most relevant first
    return sorted(recommendations, key=lambda x: x['score'], reverse=True)