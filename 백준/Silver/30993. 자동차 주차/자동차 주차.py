def fac(n):
    if n == 1:
        return n
    return n * fac(n-1)

N, A, B, C = map(int, input().split())
print(int(fac(N) / (fac(A) * fac(B) * fac(C))))