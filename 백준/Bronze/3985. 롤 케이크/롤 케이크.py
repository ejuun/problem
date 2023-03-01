L = int(input())
N = int(input())

cake = [0] * (L+1)
num = 1
expect_longest = 0
longest_idx = 0

take = dict()

for _ in range(N):
    p, k = map(int, input().split())

    if expect_longest < k - p:
        expect_longest = k - p
        longest_idx = num

    for i in range(p, k+1):
        if not cake[i]:
            cake[i] = num
    num += 1

for cnt in cake:
    if cnt != 0 and cnt not in take:
        take[cnt] = 1
    elif cnt != 0 and cnt in take:
        take[cnt] += 1

print(longest_idx)
print(max(take, key=take.get))