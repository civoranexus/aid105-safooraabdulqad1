"""
SchemeAssist AI - Simple test script for SchemeAssist AI API logic.
This script tests the recommender without using the frontend.
"""

from csv_loader import load_schemes
from recommender import recommend_schemes
from user_profile import create_user_profile

# Sample user profile
user = create_user_profile(
    age=30,
    income=200000,
    state="Telangana",
    category="Farmer",
    gender="Male")

# Load scheme data
schemes = load_schemes("data/schemes.csv")

# Get recommendations
results = recommend_schemes(user, schemes)

# Print results
for scheme in results:
    print(scheme)
