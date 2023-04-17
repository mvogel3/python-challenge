import os
import csv

file_path = os.path.join("Resources", "election_data.csv")
print(file_path)


with open(file_path) as file:
    csvreader = csv.reader(file, delimiter = ",")

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header[0]}")

    vote_count = 0
    candidate_len = 0

    ballot_id = []
    county = []
    candidate_name = []
    total_count = []
    percent_votes = []

    win_candidate = 0
    results = 0
    i = 0
    loop2 = 0
    loop3 = 0
    loop4 = 0

    for row in csvreader:
        vote_count = vote_count + 1
        ballots = row[0]
        ballot_id.append(ballots)
        counties = row[1]
        county.append(counties)
        candidate = row[2]
        candidate_name.append(candidate)
        # if candidate in candidate_name:
        #     print(candidate)

# candidate_name.append(candidate[0])
candidate_len = len(ballot_id)
for i in range(candidate_len - 1):
    if candidate[i + 1] != candidate[i] and candidate[i + 1] not in candidate_name:
        candidate_name.append(candidate[i + 1])

n = len(candidate_name)

for loop2 in range(n):
    total_count.append(candidate_name.count(candidate_name[loop2]))


for loop3 in range(n):
    percent_votes.append(f"{round((total_count[loop3]/candidate_len*100), 3)}%")
    if total_count[loop3] > win_candidate:
        winner = candidate_name[loop3]
        win_candidate = total_count[loop3]

for loop4 in range(n):
    results.append(f"{candidate_name[loop4]}: {percent_votes[loop4]} ({total_count[loop4]})")



print(vote_count)