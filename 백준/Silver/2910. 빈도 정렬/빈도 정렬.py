import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))
l_s_arr = list(set(arr))
dic = {i: [0, -1, i] for i in l_s_arr}

for i in range(len(arr)):
    if dic[arr[i]][1] == -1:
        dic[arr[i]][1] = i
    dic[arr[i]][0] += 1

sort_dic = sorted(dic.values(), key=lambda x : (-x[0], x[1]))

ans = []
for lst in sort_dic:
    for _ in range(lst[0]):
        ans.append(lst[2])
print(*ans)