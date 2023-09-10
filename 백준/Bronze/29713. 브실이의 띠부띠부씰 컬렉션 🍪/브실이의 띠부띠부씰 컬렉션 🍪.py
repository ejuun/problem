import sys

input = sys.stdin.readline

N = int(input())
alphabet = {'B': 0, 'R': 0, 'O': 0, 'N': 0, 'Z': 0, 'E': 0, 'S': 0, 'I': 0, 'L': 0, 'V': 0}

words = input().rstrip()

for word in words:
    if word in alphabet:
        alphabet[word] += 1

ans = 1000
for key, value in alphabet.items():
    if key == 'R' or key == 'E':
        value = value // 2

    if value == 0:
        ans = 0
        break
    else:
        if ans > value:
            ans = value

print(ans)