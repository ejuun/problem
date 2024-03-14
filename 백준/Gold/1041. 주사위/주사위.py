N = int(input())
sq = list(map(int, input().split()))
min_val = min(sq)
max_val = max(sq)
if N == 1:
    ans = sum(sq) - max_val
else:
    two_able = []
    for i in range(6):
        for j in range(i, 6):
            if i != j:
                if (i == 0 and j == 5) or (i == 1 and j == 4) or (i == 2 and j == 3):
                    continue
                two_able.append((i, j))
    tri_able = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]

    two_sum = tri_sum = 150
    for i, j in two_able:
        if two_sum > sq[i] + sq[j]:
            two_sum = sq[i] + sq[j]
    for i, j, k in tri_able:
        if tri_sum > sq[i] + sq[j] + sq[k]:
            tri_sum = sq[i] + sq[j] + sq[k]

    one = ((N - 2) ** 2 + 4 * (N - 1) * (N - 2)) * min_val
    two = (4 * (N - 2) + 4 * (N - 1)) * two_sum
    three = 4 * tri_sum

    ans = one + two + three

print(ans)