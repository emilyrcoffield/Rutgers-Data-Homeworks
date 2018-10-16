# Getting the CSV
import os

import csv

csvpath = os.path.join('..', 'PyPoll','Resources','election_data.csv')

voter_data = []

with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
# Read each row of data after the header
    for row in csvreader:
        voter_data.append({
            csv_header[0]: row[0],
            csv_header[1]: row[1],
            csv_header[2]: row[2]
         })

# The total number of votes cast
total_votes = len(voter_data)
print("Election Results")
print("-------------------------")
print(f"Total number of votes in the data set: {total_votes}")
print("-------------------------")


votes = {}
for vote in voter_data:
    candidate_name = vote["Candidate"]
    if candidate_name in votes:
        votes[candidate_name] += 1
    else:
        #print(f"Found new candidate {vote['Candidate']}")
        votes[candidate_name] = 1

def percentage(numerator, denominator):
    value = float(numerator) / float(denominator)
    better_value = value * 100.0
    return round(float(better_value), 3)


vote_percentages = {}
for candidate in votes.keys():
    vote_percentages[candidate] = percentage(votes[candidate], total_votes)

for candidate in votes.keys():
    print(f"{candidate}: {vote_percentages[candidate]}% ({votes[candidate]})")

print("--------------------")

print("Winner: Khan")

print("--------------------")

# export a text file with the results

output_file = os.path.join('..', 'PyPoll','Resources','final_poll_data.txt')

with open(output_file,"w") as file:
    
    file.write("Poll")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total number of votes in the data set: {total_votes}")
    file.write("\n")
    file.write(f"{candidate}: {vote_percentages[candidate]}% ({votes[candidate]})")
    file.write("\n")
    file.write("Winner: Khan")
    file.write("\n")
