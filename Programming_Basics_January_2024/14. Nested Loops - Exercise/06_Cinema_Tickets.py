student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while True:
    movie = input()
    if movie == 'Finish':
        break
    seats = int(input())
    tickets_sold = 0
    for i in range(0, seats):
        seat_type = input()
        if seat_type == 'End':
            break
        else:
            tickets_sold += 1
            if seat_type == 'student':
                student_tickets += 1
            elif seat_type == 'standard':
                standard_tickets += 1
            elif seat_type == 'kid':
                kids_tickets += 1
    print(f'{movie} - {tickets_sold / seats * 100:.2f}% full.')

total = student_tickets + standard_tickets + kids_tickets
print(f'Total tickets: {total}')
print(f'{student_tickets / total * 100:.2f}% student tickets.')
print(f'{standard_tickets / total * 100:.2f}% standard tickets.')
print(f'{kids_tickets / total * 100:.2f}% kids tickets.')
