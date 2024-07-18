students = {}
while True:
    line_students = input().split(":")
    if len(line_students) < 3:
        for key, value in students.items():
            if value[1].split(" ") == line_students[0].split("_"):
                print(f"{key} - {value[0]}")
        break
    students[line_students[0]] = [line_students[1], line_students[2]]

