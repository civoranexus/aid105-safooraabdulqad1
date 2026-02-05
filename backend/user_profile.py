"""
SchemeAssist AI - User Profile Module
This module defines the basic structure of a user profile
used for scheme recommendations.
"""

def create_user_profile(age, income, state, category, gender):
    """
    Create and return a user profile dictionary.
    """
    return {
        "age": age,
        "income": income,
        "state": state,
        "category": category,
        "gender": gender
    }
