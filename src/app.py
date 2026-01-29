from core.scheme_loader import load_schemes
from core.recommender import recommend_schemes
from reports.report_writer import write_report

def main():
    user_profile = {
        "age": 20,
        "income": 180000,
        "state": "Telangana",
        "category": "Student"
    }

    schemes = load_schemes("src/data/schemes.csv")
    recommendations = recommend_schemes(user_profile, schemes)

    if recommendations:
        top = recommendations[0]
        write_report(
            user_profile=user_profile,
            scheme=top["scheme_name"],
            score=top["score"],
            reasons=top["reasons"],
            path="src/reports/final_report.txt"
        )

    for r in recommendations:
        print("Scheme:", r["scheme_name"])
        print("Score:", r["score"])
        print("Reasons:")
        for reason in r["reasons"]:
            print("-", reason)
        print("-" * 40)

if __name__ == "__main__":
    main()
