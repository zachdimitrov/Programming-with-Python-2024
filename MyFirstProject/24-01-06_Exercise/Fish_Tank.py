length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height * 0.001
print(volume * (1 - (percent/100)))
