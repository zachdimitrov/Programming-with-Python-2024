orders = {}
while True:
    command = input()
    if command == "buy":
        for order, data in orders.items():
            print(f"{order} -> {data[0] * data[1]:.2f}")
        break
    items = command.split(" ")
    product = items[0]
    price = float(items[1])
    quantity = int(items[2])

    if product not in orders:
        orders[product] = [price, quantity]
    else:
        orders[product][0] = price
        orders[product][1] += quantity
