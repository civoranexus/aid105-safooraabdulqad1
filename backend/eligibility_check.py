"""
SchemeAssist AI - Eligibility Check Module
This module provides basic rule-based eligibility checks
between a user profile and a government scheme.
"""

def is_eligible(user_profile, scheme):
    """
    Returns True if the user is eligible for the scheme,
    otherwise returns False.
    """

    # Income check
    income = int(user_profile["income"])
    min_income = int(scheme.get("min_income", 0))
    max_income = int(scheme.get("max_income", income))

    if not (min_income <= income <= max_income):
        return False

    # State check
    scheme_state = scheme.get("state", "ALL")
    if scheme_state != "ALL" and scheme_state != user_profile["state"]:
        return False

    # Category check
    scheme_category = scheme.get("category", "ALL")
    if scheme_category != "ALL" and scheme_category != user_profile["category"]:
        return False

    return True
