
#grabbing the tools necessary for the rest of the code to function
import os
import csv
import sys

# File path
pybank_csv = os.path.join("budget_data.csv")
output_file_path = "E:\\Files\\Data Analytics\\Week 3\\Module 3 assignment\\Starter_Code\\PyBank\\Analysis\\Analysis.txt"

# Defining storage lists for the variables in the spreadsheet
changes = []
months = []
total = 0
last_row = 0
greatest_increase = 0
# positive infinity fixes an issue I had with setting it to 0
greatest_decrease = float('inf') 

with open(pybank_csv) as file:
    # Split the data on commas
    csvreader = csv.reader(file, delimiter=",")
    # Skip the header line
    header = next(csvreader)
    for row in csvreader:
        # Using the append idea from the conditional logic class example
        months.append(row[0])
        # You must turn it into int because python takes every input as a string
        loss = int(row[1])
        total = total + loss
        diff = loss - last_row
        changes.append(diff)

        # Checks and stores greatest increase and the months
        if diff > greatest_increase:
            greatest_increase = diff
            greatest_month = row[0]
        if diff < greatest_decrease:
            greatest_decrease = diff
            worst_month = row[0]

        # Resetting the last row for the next iteration
        last_row = loss

average_change = sum(changes) / len(changes)
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_month} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_month} $({greatest_decrease})")
#Redirects stdout which is the standard output, allows me to assign python to write somewhere else which means the prints will go into the designated text file in the path. 
#'w' is to enable write mode
with open(output_file_path, 'w') as output_file:
    sys.stdout = output_file

    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_month} $({greatest_increase})")
    print(f"Greatest Decrease in Profits: {worst_month} $({greatest_decrease})")

# Reset stdout to the console
sys.stdout = sys.__stdout__
