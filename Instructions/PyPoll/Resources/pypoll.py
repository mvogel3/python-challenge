import os
import csv

file_path = os.path.join("Resources"/"election_data.csv")
print(file_path)

with open(file_path) as file:
    csvreader = csv.reader(file, delimiter = ",")