import csv

def csv_columns(filename):
    columns = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for header in headers:
            columns[header] = []
        for row in reader:
            for i, value in enumerate(row):
                columns[headers[i]].append(value)
    return columns