def student_result(marks):
    if marks >= 90:
        return "Distinction"
    elif marks >= 75:
        return "First Class"
    elif marks >= 50:
        return "Passed"
    else:
        return "Fail"


students = [
    {"name": "Rahul", "marks": 95},
    {"name": "Anita", "marks": 81},
    {"name": "Kiran", "marks": 67},
    {"name": "Priya", "marks": 42},
    {"name": "Suresh", "marks": 92},
    {"name": "Tushar", "marks": 75},
    {"name": "Lavanya", "marks": 90}
]

distinction = 0
first_class = 0
passed = 0
fail = 0

for student in students:
    result = student_result(student["marks"])
    print(student["name"], "-", result)

    if result == "Distinction":
        distinction = distinction + 1
    elif result == "First Class":
        first_class = first_class + 1
    elif result == "Passed":
        passed = passed + 1
    else:
        fail = fail + 1

print()
print("Summary Report")
print("----------------")
print("Total Distinction:", distinction)
print("Total First Class:", first_class)
print("Total Passed:", passed)
print("Total Fail:", fail)
