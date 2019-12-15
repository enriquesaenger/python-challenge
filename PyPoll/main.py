# temporary variables
totalVotes = 0
khanTotal = 0
correyTotal = 0
liTotal = 0
otooleyTotal = 0

khanPercent = 0
correyPercent = 0
liPercent = 0
otooleyPercent = 0

winner = "Yo momma"













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
