rows = int(input())
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split(", "))))
    #matrix.append([y for y in [int(x) for x in input().split(", ")] if y % 2 == 0])
evens = [[x for x in row if x % 2 == 0] for row in matrix]
#print(matrix)
print(evens)
