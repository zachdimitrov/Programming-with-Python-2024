size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
diagonal = 0
for i in range(size):
    diagonal += matrix[i][i]

print(diagonal)

# another way to construct
# matrix = [[0] * size for row in range(size)]