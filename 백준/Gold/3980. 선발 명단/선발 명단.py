def back(k, hap):
    global ans

    if k == 11:
        if ans < hap:
            ans = hap
            return
        return

    for i in range(11):
        if not visited[i] and m[k][i]:
            visited[i] = 1
            back(k + 1, hap + m[k][i])
            visited[i] = 0

for _ in range(int(input())):
    m = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    ans = 0
    
    back(0, 0)
    
    print(ans)