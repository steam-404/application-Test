import csv


def read_file():
    data = []
    with open('testdata.csv', 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            data.append(i)
    return data
