import pyfiglet
import numpy as np

text_to_print = input()
result = pyfiglet.figlet_format(text_to_print, font="slant")
print(result)

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.shape)
