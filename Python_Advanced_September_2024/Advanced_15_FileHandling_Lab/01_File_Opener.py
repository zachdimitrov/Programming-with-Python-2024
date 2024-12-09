import os
from constants import ABSTRACT_PATH

path = os.path.join(ABSTRACT_PATH, "text.txt")

try:
    file = open(path)
    content = file.read(2)
    file.seek(0) #vryshta v nulata
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found")
