rows = int(input())

# matrix = []
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
flattened = [num for row in matrix for num in row]
print(flattened)

