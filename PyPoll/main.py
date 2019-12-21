import os
import os.path
from os import path
import csv

csv_path = os.path.join("Resources", "election_data.csv")

# initializing variables
candidateDict = {}
totalVotes = 0

# open csv file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    header = next(csvreader)

    # loop through rows in csv
    for row in csvreader:

        # variable for name in current row
        name = row[2]

        # check if name is already in dictionary
        if name in candidateDict:
            # if it's not there, add it
            candidateDict[name] += 1
        else:
            # if it is there, add 1 to votes
            candidateDict.update({name: 1})

# loop through dictionary and count total votes
for votes in candidateDict:
    totalVotes += candidateDict[votes]

# determine winner
winner = max(candidateDict, key = candidateDict.get)

# print first part of Election Results and assign to electionResults
electionResults = "Election Results" + '\n' \
+ "-------------------------" + '\n' \
+ "Total Votes: " + str(totalVotes) + '\n' \
+ "-------------------------" + '\n'

# loop through dictionary and add individual results to electionResults
for candidate in candidateDict:
    # calculate individual percentage and assign to percent
    percent = (candidateDict[candidate] / totalVotes) * 100
    # round percent
    round = percent.__round__(3)
    # add each candidate's results to electionResults
    electionResults += candidate + ": " + '%.3f'%round + "%" \
        + " (" + str(candidateDict[candidate]) + ")" + '\n'

# add winner to electionResults
electionResults += "-------------------------" + '\n' \
                    + "Winner: " + winner + '\n' \
                    + "-------------------------"

# print electionResults
print(electionResults)

# export a text file with electionResults
# check if Output folder exists
if os.path.exists("Output") == True:
    # join Output and Election Results.txt
    path = os.path.join("Output", "Election Results.txt")
    # create file
    f = open(path, "w+")
# if Output folder does not exist
else:
    # create Output folder
    os.mkdir("Output")
    # join Output and Election Results.txt
    path = os.path.join("Output", "Election Results.txt")
    # create file
    f = open(path, "w+")
# write electionResults to Election Results.txt
f.write(electionResults)
# close .txt file
f.close()
