
#importing the systems to utilize the code properly
import os
import csv
#file path

pybank_csv = os.path.join("Resources", "budget_data.csv")
profits = []
months = []
changes = []



with open(pybank_csv) as pybank_storage:
#split the data on commas
    csvreader = csv.reader(pybank_storage, delimiter = ",")
#skip the header line
    header = next(csvreader)
    for row in csvreader :
 #using the append idea from the conditional logic class example

        months.append(row[0])
        profits.append(row[1])       
        print(months)
        print(profits)
        