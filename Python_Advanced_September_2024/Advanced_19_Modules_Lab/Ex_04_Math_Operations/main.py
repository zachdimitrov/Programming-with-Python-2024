from Advanced_19_Modules_Lab.Ex_04_Math_Operations.core import execute

expression = input()
num1, sign, num2 = expression.split()
num1 = int(num1)
num2 = int(num2)

print(f"{execute(num1, sign, num2):.2f}")
