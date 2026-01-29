def write_report(user, scheme_name, score, reasons, path):
    with open(path, "w") as f:
        f.write(f"Scheme: {scheme_name}\n")
        f.write(f"Score: {score}\n")
        f.write("Reasons:\n")
        for r in reasons:
            f.write(f"- {r}\n")

