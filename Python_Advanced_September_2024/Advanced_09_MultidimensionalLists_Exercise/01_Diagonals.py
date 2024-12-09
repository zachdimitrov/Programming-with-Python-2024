size = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(size)]
prim_diagonal = []
sec_diagonal = []
for i in range(size):
    prim_diagonal.append(matrix[i][i])
    sec_diagonal.append(matrix[i][-(i + 1)])

print(f"Primary diagonal: {', '.join([str(x) for x in prim_diagonal])}. Sum: {sum(prim_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in sec_diagonal])}. Sum: {sum(sec_diagonal)}")
