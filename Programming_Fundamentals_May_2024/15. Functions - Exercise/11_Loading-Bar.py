n = int(input())

if n == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    bar = ""
    for i in range(n//10):
        bar += "%"
    for j in range(10 - n//10):
        bar += "."
    print(f"{n}% [{bar}]")
    print("Still loading...")
