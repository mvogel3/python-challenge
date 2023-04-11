import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")
print(file_path)
month_count = 0
total_sum = 0

previous_value = 0
revenue_change = []

max_profit = 0

with open(file_path) as file:
    csvreader = csv.reader(file, delimiter = ",")

#returns the column headers
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header[0]}")
    print(f"value before loop {revenue_change}")

#returns data in the csv using the delimiter
    for row in csvreader:
        current_value = int(row[1])
        #print(row[0]) # first item in the list
        month_count = month_count + 1
        print(f"value next iteration {previous_value}")
        print(current_value) #second value in the list
        total_sum = total_sum + current_value #allows the second value in each list to be read as an integer and added to total_sum
        print(type(revenue_change))
        if previous_value !=0:
            print("inside conditional")
            change = previous_value + current_value
            revenue_change.append(change)
            print(revenue_change)
        print("outside conditional")
        previous_value = current_value
        print(previous_value)
        # revenue_change = total_sum - current_value
# average_change = revenue_change / month_count
        #print(f"value next {total_sum}") # value after the for loop is complete
print(month_count)
print(total_sum)
print(revenue_change)
print(average_change)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: {total_sum}")
#print("Average Change: ")
#print("Greatest Increase in Profits: ")
#print("Greatest Decrease in Profits: ")