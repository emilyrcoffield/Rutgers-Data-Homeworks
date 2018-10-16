# Getting CSV data from: 
#C:\Users\emily\Documents\RUTJER201809DATA3\03-Python\Homework\Instructions\PyBank\Resources\budget_data.csv

import os

import csv

csvpath = os.path.join('..','LearnPython','PyBank','Resources','budget_data.csv')

data = []


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        data.append({
            csv_header[0]: row[0],
            csv_header[1]: int(row[1])
        })
# print(f"Data List: {data}")

#Formatting
print("------------------")
print("Financial Analysis")
print("------------------")

#The total number of months included in the dataset
print(f"Total number of months in the data set: {len(data)}")
# print(data)

total = 0
for datum in data:
    total += datum['Profit/Losses']
print(f"The total is: {total}")


#The average change in "Profit/Losses" between months over the entire period
x = 1
pl_total = 0
while x < len(data):
    diff = data[x]['Profit/Losses'] - data[x-1]['Profit/Losses']
    pl_total += diff
    x += 1

delta = pl_total / int(len(data) - 1)
print(f"Average Change:  ${round(delta, 2)}")
#---------------------------------------------------------------all good above

#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

min = data[0]['Profit/Losses']
min_date = data[0]['Date']
max = data[0]['Profit/Losses']
max_date = data[0]['Date']

x=1
while x < len(data):
    diff = data[x]['Profit/Losses'] - data[x-1]['Profit/Losses']
    data[x]['Differences'] = diff
    x += 1

delta = pl_total / int(len(data) - 1)

for datum in data:
    if 'Differences' in datum:
        taco = datum['Differences']
        if taco > max:
            max = taco
            max_date = datum['Date']
        if taco < min:
            min = taco
            min_date = datum['Date']

print(f"Greatest Increase in Profits: {max_date} (${max})")

print(f"Greatest Decrease in Profits: {min_date} (${min})")

# export a text file with the results

output_file = os.path.join('..','LearnPython','PyBank','Resources','final_budget_data.txt')

with open(output_file,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(data)}")
    file.write("\n")
    file.write(f"Total: ${total}")
    file.write("\n")
    file.write(f"Average Change: {round(delta, 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_date} (${(str(max))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_date} (${(str(min))})")