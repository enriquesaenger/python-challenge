import os
import os.path
from os import path
import csv

# define path for csv
csvpath = os.path.join("Resources", "budget_data.csv")

# lists to compare values
profitColumn = []
monthColumn = []

# initialize variables
months = 0
total = 0
totalChange = 0
greatestProfit = 0
greatestLoss = 0

# open csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    header = next(csvreader)

    # loop through rows in csvreader
    for row in csvreader:

        # count number of months
        months += 1

        # find currentProfit
        currentProfit_month = row[0]
        currentProfit_value = row[1]

        # add up total Profit/Losses
        total += int(currentProfit_value)

        # append to profitColumn and monthColumn
        profitColumn.append(currentProfit_value)
        monthColumn.append(currentProfit_month)

    # calculate length of profitColumn
    profitColumn_length = len(profitColumn)

    # loop through profitColumn to calculate change
    for profit in range(1, profitColumn_length):
        change = int(profitColumn[profit]) - int(profitColumn[profit - 1])

        # Calculate greatest increase in profits and
        # greatest decrease in profits
        if change > greatestProfit:
            greatestProfit = change
            greatestProfit_month = monthColumn[profit]
        elif change < greatestLoss:
            greatestLoss = change
            greatestLoss_month = monthColumn[profit]

        # add change to totalChange
        totalChange += change

# calculate averageChange
averageChange = totalChange / (months - 1)
# round averageChange
averageChange_rounded = averageChange.__round__(2)

# create financialAnalysis printout
financialAnalysis = (f"""Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${averageChange_rounded}
Greatest Increase in Profits: {greatestProfit_month} (${greatestProfit})
Greatest Decrease in Profits: {greatestLoss_month} (${greatestLoss})""")

# print financialAnalysis to terminal
print(financialAnalysis)

# export a text file with financialAnalysis
if os.path.exists("Output") == True:
    path = os.path.join("Output", "Financial Analysis.txt")
    f = open(path, "w+")
else:
    os.mkdir("Output")
    path = os.path.join("Output", "Financial Analysis.txt")
    f = open(path, "w+")
f.write(financialAnalysis)
f.close()
