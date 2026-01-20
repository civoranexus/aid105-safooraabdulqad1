"""
SchemeAssist AI - Flask API
This module exposes the recommendation engine
through a simple REST API.
"""

from flask import Flask, request, jsonify
from csv_loader import load_schemes
from recommender import recommend_schemes

app = Flask(__name__)

@app.route("/recommend", methods=["POST"])
def recommend():
    user_profile = request.json
    schemes = load_schemes("data/schemes.csv")
    recommendations = recommend_schemes(user_profile, schemes)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
