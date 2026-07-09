def cricket_scorecard(runs):
    if runs >= 100:
        return "Century"
    elif runs >= 50:
        return "Half_Century"
    elif runs > 0:
        return "Scored"
    else:
        return "Duck"


players = [
    {"name": "Virat", "runs": 120},
    {"name": "Rohit", "runs": 75},
    {"name": "Gill", "runs": 28},
    {"name": "Dhoni", "runs": 150},
    {"name": "Hardik", "runs": 0}
]

century = 0
half_century = 0
scored = 0
duck = 0

for player in players:
    result = cricket_scorecard(player["runs"])

    print(player["name"], "-", result)

    if result == "Century":
        century += 1
    elif result == "Half_Century":
        half_century += 1
    elif result == "Scored":
        scored += 1
    else:
        duck += 1

print()
print("Summary Report")
print("----------------")
print("Total Century      :", century)
print("Total Half Century :", half_century)
print("Total Scored       :", scored)
print("Total Duck         :", duck)
