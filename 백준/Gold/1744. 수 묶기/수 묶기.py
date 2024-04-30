import sys
input = sys.stdin.readline

N = int(input())
p = []
m = []
for _ in range(N):
    n = int(input())
    if n > 0:
        p.append(n)
    else:
        m.append(n)

p.sort()
m.sort(reverse=True)

ans = 0

while len(p) >= 2:
    n1 = p.pop()
    n2 = p.pop()
    if n1 == 1 or n2 == 1:
        ans += n1 + n2
    else:
        ans += n1 * n2
if p:
    ans += p.pop()

while len(m) >= 2:
    n1 = m.pop()
    n2 = m.pop()
    ans += n1 * n2
if m:
    ans += m.pop()

print(ans)