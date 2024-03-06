juri = int(input())
courses_count = 0
all_grades = 0

while True:
    current_grades = 0
    command = input()
    if command == 'Finish':
        break
    courses_count += 1
    for i in range(0, juri):
        current_grades += float(input())
    all_grades += current_grades
    print(f'{command} - {current_grades / juri:.2f}.')
print(f'Student\'s final assessment is {all_grades / (courses_count * juri):.2f}.')

