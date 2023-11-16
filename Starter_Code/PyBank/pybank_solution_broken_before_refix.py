
#importing the systems to utilize the code properly
import os
import csv
#file path

pybank_csv = os.path.join("Resources", "budget_data.csv")
output_file_path = "E:\Files\Data Analytics\Week 3\Module 3 assignment\Starter_Code\PyBank\Analysis\Analysis.txt"
#defining storage lists for the variables in the spreadsheet
changes = []
months = []
total = 0
last_row = 0
greatest_increase = 0
greatest_decrease = 0


with open(pybank_csv) as file:
#split the data on commas
    csvreader = csv.reader(file, delimiter = ",")
#skip the header line
    header = next(csvreader)
    for row in csvreader :
 #using the append idea from the conditional logic class example

        months.append(row[0])
        #you must turn it into int because python takes every input as a string
        loss =int(row[1]) 
        total = total + loss 
        diff = total + last_row
        changes.append(diff)
      
      #checks and stores greatest increase and the months
        if diff > greatest_increase:
            greatest_increase = diff
            greatest_month = row[0]
        if diff < greatest_decrease:
            greatest_decrease = 0
            worst_month = row[0]
        #resetting the last row for the next iteration
        last_row = loss
print=(sum(changes)/len(changes))

print=("hello world")
