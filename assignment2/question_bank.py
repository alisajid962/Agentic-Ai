questions = [
    (101, "Math", 2),
    (102, "Science", 5),
    (103, "English", 8),
    (101, "Math", 2),
    (104, "", 6),
    (105, "Math", 9),
    (106, "Science", 3),
    (107, "English", 4),
    (108, "Computer", 7)
]

accepted_questions = []
seen_ids = set()
topic_count = {}

easy = 0
medium = 0
hard = 0

target = 6

for question in questions:

    qid = question[0]
    topic = question[1]
    difficulty = question[2]

    if topic == "":
        continue

    if qid in seen_ids:
        continue

    seen_ids.add(qid)

    accepted_questions.append(question)

    if topic in topic_count:
        topic_count[topic] += 1
    else:
        topic_count[topic] = 1

    if difficulty <= 3:
        easy += 1

    elif difficulty <= 6:
        medium += 1

    else:
        hard += 1

    if len(accepted_questions) == target:
        break

print("Accepted Questions")
for i in accepted_questions:
    print(i)
print()
print("Topic Wise Count")
for i in topic_count:
    print(i, "=", topic_count[i])
print()

print("Easy Questions =", easy)
print("Medium Questions =", medium)
print("Hard Questions =", hard)