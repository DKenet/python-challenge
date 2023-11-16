#grabbing the tools necessary for the rest of the code to function
import os
import csv
import sys

# File path
pypoll_csv = (os.path.join("election_data.csv"))
output_file_path = "E:\\Files\\Data Analytics\\Week 3\\Module 3 assignment\\Starter_Code\\PyPoll\\Analysis\\Analysis.txt"

#defining variables
total = 0
Diana_Degette = 0
Charles_Stockham = 0
Raymon_Doane = 0
result_text = []
#first second and third if statements to save the top three candidates

with open(pypoll_csv) as file:
    # Split the data on commas
    csvreader = csv.reader(file, delimiter=",")
    # Skip the header line
    header = next(csvreader)
    #adding to the total
    for row in csvreader:
        total = total + 1
        if row[2] == "Diana DeGette": #checking for one of three names
            Diana_Degette = Diana_Degette + 1 #adding to the total of values for the candidate
        if row[2] == "Charles Casper Stockham":
            Charles_Stockham = Charles_Stockham + 1
        if row[2] == "Raymon Anthony Doane":
            Raymon_Doane = Raymon_Doane + 1
    
    if Diana_Degette > Charles_Stockham and Diana_Degette > Raymon_Doane:
        Winner = "Diana Degette"
    elif Charles_Stockham > Diana_Degette and Charles_Stockham > Raymon_Doane:
        Winner = "Charles Casper Stockham"
    else:
        Winner = "Raymon Anthony Doane"
    #printing results

    result_text.append("Election Results")
    result_text.append("---------------------------")
    result_text.append(f"Total Votes: {total}")
    result_text.append("---------------------------")
    result_text.append(f"Charles Casper Stockham: {Charles_Stockham/total:.2%} ({Charles_Stockham}) ") # rounding decimal places
    result_text.append(f"Diana Degette: {Diana_Degette/total:.2%} ({Diana_Degette})")
    result_text.append(f"Raymond Anthony Doane: {Raymon_Doane/total:.2%} ({Raymon_Doane})")
    result_text.append("---------------------------")
    result_text.append(f"Winner: {Winner}") 
    result_text.append("---------------------------")
    for line in result_text:
        print(line)
    #exporting results to an analysis sheet

with open(output_file_path, 'w') as output_file:
    sys.stdout = output_file
    
    for line in result_text:
        print(line)
   
sys.stdout = sys.__stdout__