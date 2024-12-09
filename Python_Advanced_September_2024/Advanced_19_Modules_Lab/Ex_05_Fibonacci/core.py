def create_sequence(n):
    first_num = 0
    second_num = 1

    seq = [first_num, second_num]
    for i in range(n - 2):
        seq.append(seq[-1] + seq[-2])


def locate_idx_of_number(seq, number):
    try:
        return seq.index(number)
    except ValueError:
        return f"The number {number} is not in the sequence"
