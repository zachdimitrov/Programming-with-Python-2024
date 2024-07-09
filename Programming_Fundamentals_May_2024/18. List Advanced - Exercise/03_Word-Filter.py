word_seq = input().split(" ")
result = [word for word in word_seq if len(word) % 2 == 0]
for a in result:
    print(a)
