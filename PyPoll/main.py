import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

# Need to make a list that appends candidates
candidateDict = {}
totalVotes = 0
'''
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
'''

# dummy variable for Winner
winner = "Yo momma"

# open csv file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    header = next(csvreader)

    # loop through rows in csv
    for row in csvreader:

        # count total number of votes
        totalVotes += 1

        # variable for name in current row
        name = row[0]
        '''
        for name in candidateDict:
            if candidateDict[name] != name:
                candidateDict[name] = name
            else:
                candidateDict[name] += 1

                # count total number of votes per Candidate
                if row[2] == candidateDict[name]:
                    candidate1_total += 1
                elif row[2] == candidate2:
                    candidate2_total += 1
                elif row[2] == candidate3:
                    candidate3_total += 1
                elif row[2] == candidate4:
                    candidate4_total += 1
                '''

# calculate percentages
candidate1_percent = candidate1_total / totalVotes * 100
candidate2_percent = candidate2_total / totalVotes * 100
candidate3_percent = candidate3_total / totalVotes * 100
candidate4_percent = candidate4_total / totalVotes * 100

# round percentages
candidate1_round = candidate1_percent.__round__(3)
candidate2_round = candidate2_percent.__round__(3)
candidate3_round = candidate3_percent.__round__(3)
candidate4_round = candidate4_percent.__round__(3)

'''
# calculate winner
# list of candidates and votes
candidatesList = [candidate1, candidate2, candidate3, candidate4]
votesList = [candidate1_total, candidate2_total,
             candidate3_total, candidate4_total]
votesList_length = len(votesList)
for candidate in range(1, votesList_length):
    if votesList[candidate - 1] > votesList[candidate]:
        winner = candidatesList[candidate - 1]
'''

# create Election Results Printout
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

# print Election Results to terminal
print(electionResults)

# export a text file with electionResults
file = open("Output/Election Results.txt", "w")
file.write(electionResults)
file.close()
