from functools import reduce
negatives_sum = 0
positives_sum = 0
sequence = [int(x) for x in input().split()]
negatives = [x for x in sequence if x < 0]
positives = [x for x in sequence if x > 0]
if len(negatives) >= 2:
    negatives_sum = reduce(lambda x, y: x + y, negatives)
elif len(negatives) == 1:
    negatives_sum = negatives[0]

if len(positives) >= 2:
    positives_sum = reduce(lambda x, y: x + y, positives)
elif len(positives) == 1:
    positives_sum = positives[0]

print(negatives_sum)
print(positives_sum)
if abs(negatives_sum) > positives_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
