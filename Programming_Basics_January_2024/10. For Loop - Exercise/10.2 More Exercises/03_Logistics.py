load_count = int(input())
micro_load = 0
truck_load = 0
train_load = 0

for i in range(0, load_count):
    days_load = int(input())
    if days_load <= 3:
        micro_load += days_load
    elif 4 <= days_load <= 11:
        truck_load += days_load
    elif days_load >= 12:
        train_load += days_load

micro_load_price = micro_load * 200
truck_load_price = truck_load * 175
train_load_price = train_load * 120

all_tons_price = micro_load_price + truck_load_price + train_load_price

all_tons = micro_load + train_load + truck_load

print(f'{all_tons_price / all_tons:.2f}')

print(f'{micro_load/all_tons * 100:.2f}%')
print(f'{truck_load/all_tons * 100:.2f}%')
print(f'{train_load/all_tons * 100:.2f}%')
