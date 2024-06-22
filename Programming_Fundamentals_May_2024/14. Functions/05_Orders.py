def calculate(ordr, cnt):
    if ordr == "coffee":
        return cnt * 1.5
    elif ordr == "water":
        return cnt * 1.0
    elif ordr == "coke":
        return cnt * 1.4
    elif ordr == "snacks":
        return cnt * 2.0


order = input()
count = int(input())

print(f'{calculate(order, count):.2f}')
