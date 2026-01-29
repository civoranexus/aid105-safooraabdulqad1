import csv

def load_schemes(csv_path):
    schemes = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["max_income"] = int(row["max_income"])
            row["priority_weight"] = int(row["priority_weight"])
            schemes.append(row)

    return schemes

