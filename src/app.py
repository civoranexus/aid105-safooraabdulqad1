from flask import Flask, request, jsonify
from flask_cors import CORS
from core.scheme_loader import load_schemes
from core.recommender import recommend_schemes
from reports.report_writer import write_report
import os

app = Flask(__name__)
CORS(app) # This allows your frontend to access the backend

# Load data once at startup
SCHEMES = load_schemes("src/data/schemes.csv")

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        user_profile = request.json
        # Step 1: Generate recommendations
        recommendations = recommend_schemes(user_profile, SCHEMES)

        # Step 2: Auto-generate report for the top result (Optional)
        if recommendations:
            top = recommendations[0]
            # Ensure directory exists
            os.makedirs("src/reports", exist_ok=True)
            write_report(
                user=user_profile,
                scheme_name=top["scheme_name"],
                score=top["score"],
                reasons=top["reasons"],
                path="src/reports/latest_api_report.txt"
            )

        return jsonify(recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)