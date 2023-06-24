s1 = '=' + input()
s2 = '-' + input()

len_s1 = len(s1)
len_s2 = len(s2)

arr = [[0 for _ in range(len_s2)] for _ in range(len_s1)]

for i in range(1, len_s1):
    for j in range(1, len_s2):
        if s1[i] == s2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
ans = 0

for line in arr:
    if ans < max(line):
        ans = max(line)

print(ans)