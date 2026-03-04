students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Clara", 90),
    ("David", 60),
    ("Eva", 45)
]

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

for student in students:
    name = student[0]
    score = student[1]
    grade = get_grade(score)
    print("Name:", name, "| Score:", score, "| Grade:", grade)