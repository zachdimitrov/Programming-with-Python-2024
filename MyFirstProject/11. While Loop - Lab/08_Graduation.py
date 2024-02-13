student = input()
klas = 1
times = 0
all_grades = 0
while True:
    grade = float(input())
    if grade < 4:
        times += 1
        if times > 1:
            print(f'{student} has been excluded at {klas} grade')
            break
    else:
        all_grades += grade
        if klas >= 12:
            print(f'{student} graduated. Average grade: {all_grades / klas:.2f}')
            break
        klas += 1
