key = int(input())
n = int(input())
message = ''
for i in range(0, n):
    message += chr(ord(input()) + key)
print(message)
