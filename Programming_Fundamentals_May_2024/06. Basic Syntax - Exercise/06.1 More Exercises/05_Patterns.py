import math
execute = int(input("Input function code: \n"
                    "1 - right arrow \n"
                    "2 - right angle triangle \n"
                    "3 - hollow figure \n"
                    "4 - diamond \n"
                    "5 - pyramid \n"
                    "6 - left angle triangle \n"
                    "7 - heart \n"))


# 01. print right arrow
def right_arrow():
    size = int(input('Input size (2 - 100): '))
    for i in range(size + 1):
        print(i * '*')
    for j in range(size - 1, 0, -1):
        print(j * '*')


# 02. print right angle triangle
def right_angle():
    size = int(input('Input size (2 - 100): '))
    for i in range(size + 1):
        print(i * '*')


# 03. print hollow pipe
def hollow_pipe():
    size = int(input('Input size (2 - 100): '))
    for i in range(size):
        if i == 0 or i == size - 1:
            print(size * '*')
        else:
            print('*' + (size - 2) * ' ' + '*')


# 04. print diamond
def diamond():
    size = int(input('Input half height (1 - 101): '))

    for i in range(1, size * 2, 2):
        print(math.floor((size * 2 - i) * 0.5) * ' ' + i * '*')
    for j in range(size * 2 - 3, 0, -2):
        print(math.floor((size * 2 - j) * 0.5) * ' ' + j * '*')


# 05. print pyramid
def pyramid():
    size = int(input('Input height (1 - 101): '))

    for i in range(1, size * 2, 2):
        print(math.floor((size * 2 - i) * 0.5) * ' ' + i * '*')


# 06. print left angle triangle
def left_angle():
    size = int(input('Input size (2 - 100): '))
    for i in range(size, 0, -1):
        print(i * '*')


# 07. print heart
def heart_pattern():
    for y in range(15, -15, -1):
        line = ''
        for x in range(-30, 30):
            if (((x * 0.04) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.04) ** 2 * (y * 0.1) ** 3) <= 0:
                line += '*'
            else:
                line += ' '
        print(line)


if execute == 1:
    right_arrow()
elif execute == 2:
    right_angle()
elif execute == 3:
    hollow_pipe()
elif execute == 4:
    diamond()
elif execute == 5:
    pyramid()
elif execute == 6:
    left_angle()
elif execute == 6:
    heart_pattern()
