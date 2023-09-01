word = input()
N = int(input())
rings = []
for _ in range(N):
    ring = input()
    rings.append(ring+ring)

ans = 0
for words in rings:
    if word in words:
        ans += 1
print(ans)