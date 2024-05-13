period = int(input())
doctors = 7
treated = 0
untreated = 0

for i in range(1, period + 1):
    if i % 3 == 0:
        if untreated > treated:
            doctors += 1

    patients = int(input())
    treated_today = 0
    if patients > doctors:
        treated_today = doctors
    else:
        treated_today = patients

    treated += treated_today

    #print('-----debugger-----')
    #print(f'patients - {patients}')
    #print(f'day {i}: treated - {treated}, untreated - {untreated}')
    #print(f'today - {treated_today}')
    #print('----end debugger---')

    if patients > treated_today:
        untreated = untreated + patients - treated_today

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')
