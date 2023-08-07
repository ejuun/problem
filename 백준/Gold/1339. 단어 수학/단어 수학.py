N = int(input())
words = []
for i in range(N):
    word = list(input())
    words.append(word)

score = [0] * 26

for i in range(len(words)):
    for j in range(len(words[i])):
        score[ord(words[i][j])-ord('A')] += 10 ** (len(words[i]) - j - 1)

point = [0] * 26

for num in range(10):
    max_value = 0
    for i in range(len(score)):
        if max_value < score[i]:
            max_value = score[i]

    if not max_value:
        break
    point[score.index(max_value)] = 9 - num
    score[score.index(max_value)] = 0

ans = 0
for i in range(len(words)):
    for j in range(len(words[i])):
        ans += point[ord(words[i][j]) - ord('A')] * 10 ** (len(words[i]) - j - 1)

print(ans)