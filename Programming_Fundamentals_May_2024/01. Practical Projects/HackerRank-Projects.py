#7 Print Function
line = input().split(" ")
n = int(line[0])
m = int(line[1])

a = "-"
b = "."
c = "|"

for i in range(n // 2):
    print(((b+c+b)*(i*2 + 1)).center(m, a))

print("WELCOME".center(m, a))

for i in range(n // 2 - 1, -1, -1):
    print(((b+c+b)*(i*2 + 1)).center(m, a))

#8 Runner up
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr, reverse=True)
    best_score = sorted_arr[0]
    for i in range(len(sorted_arr)):
        if sorted_arr[i] < best_score:
            print(sorted_arr[i])
            break

#9 Students
if __name__ == '__main__':
    students = []
    second_best = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    sorted_students = sorted(students, key=lambda x: x[1])
    best_score = sorted_students[0][1]
    for i in range(1, len(sorted_students)):
        if sorted_students[i][1] > best_score:
            if not second_best:
                second_best.append(sorted_students[i])
            else:
                if second_best[0][1] == sorted_students[i][1]:
                    second_best.append(sorted_students[i])
    sorted_second_best = sorted(second_best, key=lambda x: x[0])
    for s in sorted_second_best:
        print(s[0])

#10 Scores
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_score = 0
    for name, scores in student_marks.items():
        if name == query_name:
            avg_score = sum(scores)/len(scores)
    print(f"{avg_score:.2f}")

#11 Sets Difference
n = int(input())
first_group = set(map(int, input().split(" ")))
m = int(input())
second_group = set(map(int, input().split(" ")))
result = first_group.symmetric_difference(second_group)
print(len(result))

#12
