import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")
print(file_path)

with open(file_path) as file:
    csvreader = csv.reader(file, delimiter = ",")

#returns the column headers
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#returns data in the csv using the delimiter
    for row in csvreader:
        print(row)

