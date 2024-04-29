import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
for _ in range(n):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)
ans = 0

plus.sort()
minus.sort(reverse=True)

while len(plus) >= 2:
    x = plus.pop()
    y = plus.pop()
    if x == 1 or y == 1:
        ans += x + y
    else:
        ans += x * y
if plus:
    z = plus.pop()
    ans += z

while len(minus) >= 2:
    x = minus.pop()
    y = minus.pop()
    ans += x * y
if minus:
    z = minus.pop()
    ans += z

print(ans)