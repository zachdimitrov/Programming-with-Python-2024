matrix = [[x for x in el.split()] for el in input().split("|")]
for j in range(len(matrix) - 1, -1, -1):
    if len(matrix[j]):
        print(" ".join(matrix[j]), end=" ")
