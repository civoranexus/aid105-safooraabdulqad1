def write_report(user, scheme_name, score, reasons, path):
    with open(path, "w") as f:
        f.write("SchemeAssist AI – Recommendation Report\n")
        f.write("=" * 40 + "\n\n")

        f.write("User Profile:\n")
        for k, v in user.items():
            f.write(f"- {k.capitalize()}: {v}\n")

        f.write("\nRecommended Scheme:\n")
        f.write(f"Scheme: {scheme_name}\n")
        f.write(f"Score: {score}\n")

        f.write("\nReasons:\n")
        for r in reasons:
            f.write(f"- {r}\n")
