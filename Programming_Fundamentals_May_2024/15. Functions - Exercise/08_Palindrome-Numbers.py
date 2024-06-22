def is_palindrome(st):
    for i in range(0, len(st)//2):
        if st[i] != st[len(st)-i-1]:
            return False
    return True


numbers = input().split(", ")

for elem in numbers:
    print(is_palindrome(elem))

