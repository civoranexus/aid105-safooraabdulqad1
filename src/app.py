from core.scheme_loader import load_schemes
from core.recommender import recommend_schemes
from reports.report_writer import write_report

def main():
    """
    Entry point for SchemeAssist AI.
    Executes the full recommendation pipeline.
    """

    # Step 1: Define user profile
    user_profile = {
        "age": 20,
        "income": 180000,
        "state": "Telangana",
        "category": "Student"
    }

    # Step 2: Load scheme data
    schemes = load_schemes("src/data/schemes.csv")

    # Step 3: Generate recommendations
    recommendations = recommend_schemes(user_profile, schemes)

    # Step 4: Generate report for top recommendation
    if recommendations:
        top = recommendations[0]
        write_report(
            user=user_profile,
            scheme_name=top["scheme_name"],
            score=top["score"],
            reasons=top["reasons"],
            path="src/reports/final_report.txt"
        )

    # Step 5: Display results
    for r in recommendations:
        print("Scheme:", r["scheme_name"])
        print("Score:", r["score"])
        print("Reasons:")
        for reason in r["reasons"]:
            print("-", reason)
        print("-" * 40)

if __name__ == "__main__":
    main()
