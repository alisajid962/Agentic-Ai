team_points = {}

team_set = set()

match_list = []

while True:
    team_a = input("Enter Team A: ").upper()
    if team_a == "END":
        break
    team_b = input("Enter Team B: ").upper()
    result = input("Enter Result (A/B/draw/NR): ").lower()
    if result == "nr":
        print("Match Abandoned")
        continue
    match_tuple = (team_a, team_b, result)
    match_list.append(match_tuple)
    team_set.add(team_a)
    team_set.add(team_b)

    if team_a not in team_points:
        team_points[team_a] = 0

    if team_b not in team_points:
        team_points[team_b] = 0
    if result == "a":
        team_points[team_a] += 3
    elif result == "b":
        team_points[team_b] += 3
    elif result == "draw":
        team_points[team_a] += 1
        team_points[team_b] += 1
print("Matches")
for match in match_list:
    print(match)
print("Paricipating Teams:")
print(team_set)
print("Final Points Table")
for team, points in team_points.items():
    print(team, ":", points)