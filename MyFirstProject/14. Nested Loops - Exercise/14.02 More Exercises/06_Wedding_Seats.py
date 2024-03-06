last_sector = input()
first_sector_rows = int(input())
uneven_row_seats = int(input())
sector_rows = first_sector_rows
counter = 0

for i in range(65, ord(last_sector) + 1):
    for j in range(1, sector_rows + 1):
        seats = uneven_row_seats
        if j % 2 == 0:
            seats += 2
        for k in range(97, 97 + seats):
            print(chr(i) + str(j) + chr(k))
            counter += 1
    sector_rows += 1
print(counter)
