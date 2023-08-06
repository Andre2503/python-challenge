#call modules 
import os
import csv

#define path

csvpath = os.path.join("Resources", "budget_data.csv")
outpath = os.path.join("Analysis", "Analysis.txt")

#create variables 
total_months = 0
total_profit = 0
profit = 0
change = 0
greatest_inc_month = ""
greatest_inc = 0 
greatest_dec_month = ""
greatest_dec = 0
previous_profit = 0
total_change = 0

#Open the cvs file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the header
    header = next(csvreader)


#Iterate through rows and count number of months

    for row in csvreader:
        total_months += 1 
        profit = int(row[1])
        total_profit += profit
        if total_months > 1:
            change = profit - previous_profit
            total_change += change
            if change > greatest_inc:
                greatest_inc = change
                greatest_inc_month = row[0] 
            if change < greatest_dec:
                greatest_dec = change
                greatest_dec_month = row[0]
        previous_profit = profit
        
lines = []
lines.append(f"Financial Analysis")
lines.append(f"--------------------")
lines.append(f"Total Months: {total_months}")
lines.append(f'Total: {total_profit}')
lines.append(f"Average Change: {round(total_change/(total_months -1),2)}")
lines.append(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
lines.append(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")

for line in lines:
    print(line)

#print(f"Total number of months: {total_months}")
#print(f'Total profit is: {total_profit}')
        #print(row)

with open(outpath, 'w') as outfile:
    for line in lines:
        outfile.write(line + "\n")
