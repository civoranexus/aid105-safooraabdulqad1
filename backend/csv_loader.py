"""
SchemeAssist AI - CSV Scheme Loader
This module loads government scheme data
from a CSV file for backend processing.
"""

import csv

def load_schemes(file_path):
    """
    Loads scheme data from a CSV file and returns
    it as a list of dictionaries.
    """
    schemes = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            schemes.append(row)

    return schemes
