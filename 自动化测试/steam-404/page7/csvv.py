import csv


def read_file():
    data = []
    with open('testdata.csv') as file:
        reader = csv.reader(file)
        for i in reader:
            data.append(i)
    return data
