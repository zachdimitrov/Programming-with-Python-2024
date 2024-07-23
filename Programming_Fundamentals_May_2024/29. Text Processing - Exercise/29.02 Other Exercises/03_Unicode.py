line = input()
res = ''.join(r'\u{:04X}'.format(ord(chr)) for chr in line)
print(str(res).lower())