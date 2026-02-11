from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.core.recommender import recommend_schemes
from src.core.scheme_loader import load_schemes
from src.reports.report_writer import write_report
import os

app = Flask(__name__)
CORS(app)  # Required for your index.html to communicate with the backend

# Load data from the data folder

SCHEMES_DATA = load_schemes("src/data/schemes.csv")


@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        user_profile = request.json 
        # Processes user data: Age, Income, State, Category, Gender
        results = recommend_schemes(user_profile, SCHEMES_DATA) 
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download_report", methods=["POST"])
def download_report():
    try:
        data = request.json
        user_profile = data.get('profile')
        recommendations = data.get('results')
        
        # This creates the file in your 'reports' folder
        filepath = os.path.join("reports", "scheme_report.txt")
        write_report(user_profile, recommendations, filepath)
        
        return jsonify({"message": "Report generated successfully!", "path": filepath})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure the reports folder exists for report_writer.py
    if not os.path.exists('reports'):
        os.makedirs('reports')
    app.run(debug=True, port=5000)