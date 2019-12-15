import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

# variables
candidate1 = "Khan"
candidate2 = "Correy"
candidate3 = "Li"
candidate4 = "O'Tooley"
totalVotes = 0
candidate1_total = 0
candidate2_total = 0
candidate3_total = 0
candidate4_total = 0

# temporary variables
khanPercent = 0
correyPercent = 0
liPercent = 0
otooleyPercent = 0
winner = "Yo momma"
#

# open csv file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    header = next(csvreader)

    # loop through rows in csv
    for row in csvreader:

        # count total number of votes
        totalVotes += 1

        # count total number of votes per Candidate
        if row[2] == candidate1:
            candidate1_total += 1
        elif row[2] == candidate2:
            candidate2_total += 1
        elif row[2] == candidate3:
            candidate3_total += 1
        elif row[2] == candidate4:
            candidate4_total += 1

# calculate percentages
candidate1_percent = candidate1_total / totalVotes
candidate2_percent = candidate2_total / totalVotes
candidate3_percent = candidate3_total / totalVotes
candidate4_percent = candidate4_total / totalVotes

# round percentages
candidate1_round = candidate1_percent.__round__(3)
candidate2_round = candidate2_percent.__round__(3)
candidate3_round = candidate3_percent.__round__(3)
candidate4_round = candidate4_percent.__round__(3)


electionResults = (f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
{candidate1}: {candidate1_round}% ({candidate1_total})
{candidate2}: {candidate2_round}% ({candidate2_total})
{candidate3}: {candidate3_round}% ({candidate3_total})
{candidate4}: {candidate4_round}% ({candidate4_total})
-------------------------
Winner: {winner}
-------------------------""")
print(electionResults)
