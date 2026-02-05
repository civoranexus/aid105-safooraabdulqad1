"""
SchemeAssist AI - Recommendation Report Generator
This module generates a simple text-based report
for scheme recommendations.
"""

def generate_report(user_profile, recommendations, file_path):
    """
    Generate a text report summarizing user profile
    and recommended schemes.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("SchemeAssist AI - Recommendation Report\n")
        file.write("--------------------------------------\n\n")

        file.write("User Profile:\n")
        for key, value in user_profile.items():
            file.write(f"- {key.capitalize()}: {value}\n")

        file.write("\nRecommended Schemes:\n")
        if not recommendations:
            file.write("No eligible schemes found.\n")
        else:
            for scheme in recommendations:
                file.write(
                    f"- {scheme['scheme_name']} "
                    f"(Score: {scheme['score']})\n"
                )
