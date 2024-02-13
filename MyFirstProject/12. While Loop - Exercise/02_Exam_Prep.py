bad_scores = int(input())
counter = 0
counter_all = 0
scores_all = 0
problem_name = ''

while True:
    task_name = input()
    if task_name == 'Enough':
        avg_score = scores_all / counter_all
        print(f'Average score: {avg_score:.2f}')
        print(f'Number of problems: {counter_all}')
        print(f'Last problem: {problem_name}')
        break

    problem_name = task_name
    score = int(input())
    scores_all += score
    counter_all += 1
    if score <= 4:
        counter += 1
    if counter >= bad_scores:
        print(f'You need a break, {counter} poor grades.')
        break
