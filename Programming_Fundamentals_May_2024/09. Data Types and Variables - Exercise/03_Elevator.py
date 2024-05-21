people = int(input())
capacity = int(input())

if people <= capacity:
    print('All the people fit inside the elevator. Only one course is needed.')
else:
    courses = people // capacity
    remain = people - (courses * capacity)
    # print(f'{courses} courses * {capacity} people')
    if remain > 0:
        # print(f'+ 1 course * {remain} persons')
        print(courses + 1)
    else:
        print(courses)
