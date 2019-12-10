#Dummy Variables
totalMonths = 86
total = 38382578
averageChange = -2315.12
greatestIncrease = "Feb-2012 ($1926159)"
greatestDecrease = "Sep-2013 ($-2196167)"



s = f"""
Financial Analysis
{ '-' * 28}
Total Months: {totalMonths}
Total: ${total}
Average Change: ${averageChange}
Greatest Increase in Profits: {greatestIncrease}
Greatest Decrease in Profits: {greatestDecrease}
"""
print(s)
