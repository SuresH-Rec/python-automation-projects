def candidate_rating(score):
    if score >= 90:
        return "strong_hire"
    elif score >= 75:
        return "hire"
    elif score >= 60:
        return "maybe"
    else:
        return "reject"

candidates = [
    {"name": "Arjun.R", "score": 93},
    {"name": "Divya.S", "score": 88},
    {"name": "Rohit.M", "score": 71},
    {"name": "Neha.P", "score": 58},
    {"name": "Karthik.V", "score": 65},
    {"name": "Ananya.T", "score": 79},
    {"name": "Vikram.J", "score": 84},
    {"name": "Priya.B", "score": 50}
]

strong_hire = 0
hire = 0
maybe = 0
reject = 0

for candidate in candidates:
    result = candidate_rating(candidate["score"])
    print(candidate["name"], "-", result)
    if result == "strong_hire":
        strong_hire += 1
    elif result == "hire":
        hire += 1
    elif result == "maybe":
        maybe += 1
    else:
        reject += 1

print()
print("Interview Summary Report")
print("-------------------------")
print("Total Strong Hire      :", strong_hire)
print("Total Hire             :", hire)
print("Total Maybe            :", maybe)
print("Total Reject           :", reject)
