import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")
print(file_path)
month_count = 0
total_sum = 0
with open(file_path) as file:
    csvreader = csv.reader(file, delimiter = ",")

#returns the column headers
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header[0]}")
    print(f"value before loop {month_count}")

#returns data in the csv using the delimiter
    for row in csvreader:
        #print(row[0]) # first item in the list
        month_count = month_count + 1
        print(f"value next iteration {total_sum}")
        print(row[1]) # second va;ue in the list
        total_sum = total_sum + int(row[1])
        #print(f"value next {total_sum}") # value after the for loop is complete
print(month_count)
print(total_sum)

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {month_count}")
print(f"Total: {total_sum}")
#print("Average Change: ")
#print("Greatest Increase in Profits: ")
#print("Greatest Decrease in Profits: ")