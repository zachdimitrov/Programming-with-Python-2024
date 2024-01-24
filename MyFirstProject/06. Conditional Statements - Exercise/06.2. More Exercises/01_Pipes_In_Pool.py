pool_volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours = float(input())

percent_first_pipe = (first_pipe * hours) / \
                     (first_pipe * hours + second_pipe * hours) * 100

percent_second_pipe = (second_pipe * hours) / \
                     (first_pipe * hours + second_pipe * hours) * 100

percent_pool = (first_pipe * hours + second_pipe * hours) / pool_volume * 100

if percent_pool > 100:
    liters_more = first_pipe * hours + second_pipe * hours - pool_volume
    print(f'For {hours:.2f} hours the pool overflows with {liters_more:.2f} liters.')
else:
    print(f'The pool is {percent_pool:.2f}% full. '
          f'Pipe 1: {percent_first_pipe:.2f}%. '
          f'Pipe 2: {percent_second_pipe:.2f}%.')



