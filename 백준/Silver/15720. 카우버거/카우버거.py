B, C, D = map(int, input().split())
b = list(map(int, input().split()))
s = list(map(int, input().split()))
d = list(map(int, input().split()))
b.sort(reverse=True)
s.sort(reverse=True)
d.sort(reverse=True)
m = min(len(b), len(s), len(d))

no_sale = sum(b) + sum(s) + sum(d)

total = 0
for i in range(m):
    total += int((b[i] + s[i] + d[i]) * 0.9)

for i in range(m, len(b)):
    total += b[i]
for i in range(m, len(s)):
    total += s[i]
for i in range(m, len(d)):
    total += d[i]
    
print(no_sale)
print(total)