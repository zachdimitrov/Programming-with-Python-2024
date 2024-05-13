book_to_read = input()
counter = 0

while True:
    book_found = input()
    if book_found == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {counter} books.')
        break
    if book_found == book_to_read:
        print(f'You checked {counter} books and found it.')
        break
    counter += 1
