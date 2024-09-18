size = int(input())
matrix = [[x for x in list(input())] for _ in range(size)]
searched = input()
found = False

for i in range(size):
    if found:
        break
    for j in range(size):
        if matrix[i][j] == searched:
            print(f"({i}, {j})")
            found = True

if not found:
    print(f"{searched} does not occur in the matrix")
