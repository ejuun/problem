def nQueen(k):
    global ans

    if k == N :
        ans += 1
        return
    else:
        for i in range(N):
            if row[i]:
                continue
            if not promising(k, i):
                continue
            row[i] = 1
            col[k] = i
            nQueen(k+1)
            row[i] = 0

def promising(r, c):
    for i in range(r):
        if abs(r - i) == abs(c - col[i]):
            return False
    return True

N = int(input())

ans = 0
row = [0] * N
col = [0] * N

nQueen(0)
print(ans)