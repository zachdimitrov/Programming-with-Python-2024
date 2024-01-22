pens = int(input())
markers = int(input())
soap = int(input())
discount = int(input())
full_price = (pens * 5.8) + (markers * 7.2) + (soap * 1.2)
print(full_price - (full_price * discount * 0.01))

