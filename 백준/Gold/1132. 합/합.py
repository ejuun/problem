import sys
input = sys.stdin.readline

N = int(input())
lst = []
num = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []}
hap = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
real = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
front = set()
use = set()
for _ in range(N):
    lst.append(list(input().rstrip()))

for word in lst:
    front.add(word[0])
    for i in range(len(word) - 1, -1, -1):
        num[len(word) - 1 - i].append(word[i])
        use.add(word[i])

for key, value in num.items():
    if len(value):
        for alpha in value:
            hap[alpha] += 10 ** key

use = list(use)
front = list(front)
spin = len(use)

cnt = 9
while spin > 0:
    compare = 0
    idx = ""

    for key, value in hap.items():
        if compare <= value:
            compare = value
            idx = key
    real[idx] = cnt
    hap[idx] = 0
    cnt -= 1
    spin -= 1

zero = False
change_value = 1e12
if len(use) == 10:
    for c in front:
        if real[c] == 0:
            for find in use:
                if c!= find and find not in front:
                    if change_value > real[find]:
                        change_value = real[find]
                        zero = True
if zero:
    for key, value in real.items():
        if value < change_value:
            real[key] += 1
        if value == change_value:
            real[key] = 0

ans = 0
for word in lst:
    cal = 0
    for i in range(len(word)):
        word[i] = real[word[i]]
        cal += (10 ** (len(word)-1-i) * word[i])
    ans += cal
print(ans)