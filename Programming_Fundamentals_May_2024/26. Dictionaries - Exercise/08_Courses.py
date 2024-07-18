courses = {}
while True:
    command = input()
    if command == "end":
        break
    lines = command.split(" : ")
    course_name = lines[0]
    student = lines[1]
    if course_name not in courses:
        courses[course_name] = [student]
    else:
        courses[course_name].append(student)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
