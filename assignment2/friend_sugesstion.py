friends = {}
no_of_people = int(input("Enter Number of People: "))
for i in range(no_of_people):
    person = input("Enter Person Name: ")
    no_of_friends = int(input("Enter Number of Friends: "))
    friend_set = set()
    for j in range(no_of_friends):
        friend = input("Enter Friend Name: ").upper()
        friend_set.add(friend)
    friends[person] = friend_set
person = input("\nEnter Person for Suggestions: ").upper()
suggestions = []
if person in friends:
    for candidate in friends:
        if candidate == person:
            continue
        if candidate in friends[person]:
            continue
        mutual = friends[person] & friends[candidate]
        mutual_count = len(mutual)
        if mutual_count >= 2:
            suggestion = (candidate, mutual_count)

            suggestions.append(suggestion)

        if len(suggestions) == 5:
            break
else:
    print("Person Not Found.")
print("Friend Suggestions")
for i in suggestions:
    print(i)