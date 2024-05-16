orders = int(input())
total = 0

for i in range(0, orders):
    pricePerCapsule = float(input())
    days = int(input())
    capsulesPerDay = int(input())
    if days < 1 or days > 31:
        continue
    if pricePerCapsule < 0.01 or pricePerCapsule > 100.0:
        continue
    if capsulesPerDay < 1 or capsulesPerDay > 2000:
        continue
    orderPrice = pricePerCapsule * capsulesPerDay * days
    print(f'The price for the coffee is: ${orderPrice:.2f}')
    total += orderPrice

print(f'Total: ${total:.2f}')
