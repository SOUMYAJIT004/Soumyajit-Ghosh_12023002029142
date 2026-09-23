import csv
import os

def read_test_data(file_name):
    data = []
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', file_name)
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
