students = int(input())

poor = 0
medium = 0
high = 0
excellent = 0
all_grades = 0

for i in range(0, students):
    grade = float(input())
    all_grades += grade
    if 2.00 <= grade < 3:
        poor += 1
    elif 3 <= grade < 4:
        medium += 1
    elif 4 <= grade < 5:
        high += 1
    elif grade >= 5:
        excellent += 1

print(f'Top students: {excellent / students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {high / students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {medium / students * 100:.2f}%')
print(f'Fail: {poor / students * 100:.2f}%')
print(f'Average: {all_grades / students:.2f}')
