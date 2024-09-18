num = int(input())

students = {}

for i in range(num):
    command = input().split()
    student_name = command[0]
    grade = float(command[1])
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

for key, value in students.items():
    print(f"{key} -> {' '.join([f'{el:.2f}' for el in value])} (avg: {sum(value)/len(value):.2f})")

