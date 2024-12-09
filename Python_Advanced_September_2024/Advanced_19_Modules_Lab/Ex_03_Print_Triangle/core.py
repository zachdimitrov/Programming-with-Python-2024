def print_upper_part(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()


def print_bottom_part(n):
    for row in range(1, n):
        end_num = n - row
        for col in range(1, end_num + 1):
            print(col, end=" ")
        print()


def print_triangle(n):
    print_upper_part(n)
    print_bottom_part(n)
