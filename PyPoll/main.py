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
canditate3_total = 0
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

        # count total nubmer of votes per Candidate
        if row[2] == candidate1:
            candidate1_total += 1
        elif row[2] == candidate2:
            candidate2_total += 1
        elif row[2] == candidate3:
            canditate3_total += 1
        elif row[2] == candidate4:
            candidate4_total += 1


khanPercent_round = khanPercent.__round__(3)
correyPercent_round = correyPercent.__round__(3)
liPercent_round = liPercent.__round__(3)
otooleyPercent_round = otooleyPercent.__round__(3)


electionResults = (f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
Khan: {khanPercent_round}% ({khanTotal})
Correy: {correyPercent_round}% ({correyTotal})
Li: {liPercent_round}% ({liTotal})
O'Tooley: {otooleyPercent_round}% ({otooleyTotal})
-------------------------
Winner: {winner}
-------------------------""")
print(electionResults)
