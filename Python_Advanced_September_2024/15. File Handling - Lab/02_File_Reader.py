import os
from constants import ABSTRACT_PATH

path = os.path.join(ABSTRACT_PATH, "numbers.txt")

try:
    file = open(path)
    content = [int(x) for x in file.read().split("\n") if x.isnumeric()]
    print(sum(content))
    file.close()
except FileNotFoundError:
    print("File not found")
