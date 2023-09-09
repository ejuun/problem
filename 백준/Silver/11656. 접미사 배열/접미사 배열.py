S = input()
words = []
for i in range(len(S)):
    words.append(S[i:])
words.sort()
for word in words:
    print(word)