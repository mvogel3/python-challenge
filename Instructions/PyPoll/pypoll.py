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

    i = 0

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


        
print(vote_count)