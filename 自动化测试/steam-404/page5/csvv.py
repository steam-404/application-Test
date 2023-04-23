import csv


def ReadFile():
    data = []
    with open('testdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data
