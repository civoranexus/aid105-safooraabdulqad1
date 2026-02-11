"""
SchemeAssist AI - Explanation Builder
Converts eligibility matches into human-readable reasoning.
"""

def build_explanation(user_profile, scheme):
    reasons = []
    
    # Income Reasoning
    if int(user_profile['income']) <= int(scheme.get('max_income', 9999999)):
        reasons.append(f"Your annual income (₹{user_profile['income']}) is within the eligible range.")
    
    # State Reasoning
    if scheme.get('state') == "ALL":
        reasons.append("This is a Central Government scheme applicable nationwide.")
    else:
        reasons.append(f"Applicable for residents of {user_profile['state']}.")
        
    # Category Reasoning
    if scheme.get('category') == user_profile['category']:
        reasons.append(f"Matches your social category: {user_profile['category']}.")
        
    return reasons