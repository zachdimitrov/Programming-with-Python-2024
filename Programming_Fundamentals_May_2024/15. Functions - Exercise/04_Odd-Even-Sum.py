def odd_even_sum(d):
    digits = list(map(int, list(d)))
    odd_sum = 0
    even_sum = 0
    for elem in digits:
        if elem % 2 == 0:
            even_sum += elem
        else:
            odd_sum += elem

    print(f"Odd sum = {odd_sum}", end=", ")
    print(f"Even sum = {even_sum}")


odd_even_sum(input())
