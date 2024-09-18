num = int(input())

cars = set()

for i in range(num):
    next_car = input().split(", ")
    if next_car[0] == "IN":
        cars.add(next_car[1])
    else:
        cars.remove(next_car[1])

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")