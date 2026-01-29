import csv

def load_schemes(csv_path):
    """
    Load government schemes from CSV file.
    Returns a list of scheme dictionaries.
    """
    schemes = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            schemes.append(row)

    return schemes
