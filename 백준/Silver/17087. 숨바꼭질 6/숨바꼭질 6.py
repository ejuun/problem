def great(A):
    for i in range(min(A), 0, -1):
        cnt = 0
        for j in range(len(A)):
            if A[j] % i == 0:
                cnt += 1
            else:
                break
        if cnt == len(A):
            return i

N, S = map(int, input().split())
A = list(map(int, input().split()))

i = 0
while i < N:
    A[i] = abs(S-A[i])
    i += 1

print(great(A))
