vote_count = {}
voter_ids = set()
accepted_votes = []
valid_candidates = ["Ali", "Ahmed", "Sara", "Hamza"]
no_of_votes = int(input("Enter Number of Votes: "))
for i in range(no_of_votes):
    voter_id = input("Enter Voter ID: ")
    if voter_id == "CLOSED":
        print("Voting Closed.")
        break
    candidate = input("Enter Candidate Name: ")
    vote = (voter_id, candidate)
    voter_id = vote[0]
    candidate = vote[1]
    if candidate == "":
        print("Spoiled Ballot.")
        continue

    if voter_id in voter_ids:
        print("Voter has already voted.")
        continue

    if candidate not in valid_candidates:
        print("Invalid Candidate.")
        continue

    voter_ids.add(voter_id)
    accepted_votes.append(vote)

    if candidate in vote_count:
        vote_count[candidate] += 1
    else:
        vote_count[candidate] = 1

print("\nCandidate Votes")
for i in vote_count:
    print(i, "=", vote_count[i])

winner = ""
max_votes = 0

for i in vote_count:

    if vote_count[i] > max_votes:
        max_votes = vote_count[i]
        winner = i

print("\nWinner =", winner)
print("Total Votes =", max_votes)

print("\nAccepted Votes")

for i in accepted_votes:
    print(i)
print("==============================================")
for i in vote_count:
    print(i)