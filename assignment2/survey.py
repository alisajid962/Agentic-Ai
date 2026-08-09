response_list = []
answer_count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}
respondent_set = set()
while True:
    respondent_id = input("Enter respondent id: ").upper()
    if respondent_id == "END":
        break
    answer = input("Enter answer (A/B/C/D): ").upper()
    if answer not in ["A", "B", "C", "D"]:
        print("Invalid Answer")
        continue
    if respondent_id in respondent_set:
        print("Duplicate Response")
        continue

    response_tuple = (respondent_id, answer)

    response_list.append(response_tuple)

    respondent_set.add(respondent_id)

    answer_count[answer] += 1
winner = "A"
if answer_count["B"] > answer_count[winner]:
    winner = "B"
elif answer_count["C"] > answer_count[winner]:
    winner = "C"
elif answer_count["D"] > answer_count[winner]:
    winner = "D"
print("\nResponses:")
for response in response_list:
    print(response)
print("\nAnswer Counts:")
for key, value in answer_count.items():
    print(key, ":", value)
print("Winning Option:", winner)
print("Total Valid Responses:", len(response_list))