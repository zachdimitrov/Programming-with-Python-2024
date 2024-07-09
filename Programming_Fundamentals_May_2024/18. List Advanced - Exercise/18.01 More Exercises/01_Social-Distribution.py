population = list(map(int, input().split(", ")))
min_sum = int(input())

while True:
    min_wealth = min(population)
    max_wealth = max(population)
    if max_wealth <= min_sum or min_wealth >= min_sum:
        break
    needed = min_sum - min_wealth
    available = needed
    if max_wealth + needed < min_sum:
        available = max_wealth - min_sum
    population[population.index(max_wealth)] = max_wealth - available
    population[population.index(min_wealth)] = min_wealth + available

if min(population) < min_sum:
    print("No equal distribution possible")
else:
    print(population)
