size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
prim_diagonal = 0
sec_diagonal = 0
for i in range(size):
    prim_diagonal += matrix[i][i]
    sec_diagonal += matrix[i][-(i + 1)]

print(abs(prim_diagonal - sec_diagonal))

