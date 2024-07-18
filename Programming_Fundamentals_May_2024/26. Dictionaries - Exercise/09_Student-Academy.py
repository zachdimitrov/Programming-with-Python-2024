n = int(input())
students = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for name, grades in students.items():
    avg_grade = sum(grades)/len(grades)
    if avg_grade >= 4.50:
        print(f"{name} -> {avg_grade:.2f}")
