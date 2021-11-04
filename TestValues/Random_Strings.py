import csv


def create_string_list():
    with open("Fruits.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data[0]
