words = int(input())
given_word = input()
word_list = list()
for i in range(0, words):
    current = input()
    word_list.append(current)
print(word_list)
for i in range(len(word_list) - 1, -1, -1):
    element = word_list[i]
    if given_word not in element:
        word_list.remove(element)
print(word_list)
