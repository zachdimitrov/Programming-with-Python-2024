n = int(input())
positive_numbers = list()
negative_numbers = list()
count_positive = 0
sum_negative = 0

for i in range(0, n):
    next_number = int(input())
    if next_number > 0:
        positive_numbers.append(next_number)
    else:
        negative_numbers.append(next_number)
print(positive_numbers)
print(negative_numbers)

for elm in positive_numbers:
    count_positive += 1
for elm in negative_numbers:
    sum_negative += elm

print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')
