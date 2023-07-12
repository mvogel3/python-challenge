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
    candidate_list = []

    win_candidate = 0
    results = []

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
    # print(vote_count)
    # print(candidate_name)

    candidate_list.append(candidate_name[0])
    candidate_len = len(ballot_id)
    # print(candidate)
    # print(candidate_name)

    for c in candidate_name:
        if c not in candidate_list:
            candidate_list.append(c)
    print(candidate_list)

    n = len(candidate_list)

    for loop2 in range(n):
        total_count.append(candidate_name.count(candidate_list[loop2]))
    print(total_count)


    for loop3 in range(n):
        percent_votes.append(f"{round((total_count[loop3]/candidate_len*100), 3)}%")
        if total_count[loop3] > win_candidate:
            winner = candidate_list[loop3]
            win_candidate = total_count[loop3]
    print(winner)

    for loop4 in range(n):
        results.append(f"{candidate_list[loop4]}: {percent_votes[loop4]} ({total_count[loop4]})")
    print(results)

    candidate_results = '\n'.join(results)


analysis = f'\
Election Results\n\
----------------------------\n\
Total Votes: {vote_count}\n\
----------------------------\n\
{candidate_results}\n\
----------------------------\n\
Winner: {winner}\n\
----------------------------\n'

print(analysis)
output = open('pypoll.txt', 'w')
output.writelines(analysis)
output.close()

# for r in results:
#     print(r)
# print("----------------------------")
# print(f"Winner: {winner}")
# print("----------------------------")