score = [0] * 8
for i in range(8):
    score[i] = int(input())
sort_list = sorted(score, reverse=True)

ans1 = 0
for i in range(5):
    ans1 += sort_list[i]
ans2 = []
for i in range(5):
    if sort_list[i] in score:
        ans2.append(score.index(sort_list[i])+1)
ans2.sort()
print(ans1)
print(*ans2)