"""
SchemeAssist AI - Rejection Reasons
Identifies why a user does not meet scheme criteria.
"""

def get_rejection_reasons(user_profile, scheme):
    rejections = []
    
    # Income Check
    if int(user_profile['income']) > int(scheme.get('max_income', 0)):
        rejections.append("Income exceeds the maximum limit for this scheme.")
        
    # Age Check
    age = int(user_profile['age'])
    if age < int(scheme.get('min_age', 0)) or age > int(scheme.get('max_age', 100)):
        rejections.append(f"Your age ({age}) is outside the required range.")
        
    # Category Check
    if scheme.get('category') != "ALL" and scheme.get('category') != user_profile['category']:
        rejections.append(f"Scheme is reserved for the '{scheme.get('category')}' category.")
        
    return rejections