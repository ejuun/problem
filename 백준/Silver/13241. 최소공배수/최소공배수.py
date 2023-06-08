from math import gcd

A, B = map(int, input().split())
a = A // gcd(A, B)
b = B // gcd(A, B)
ans = a * b * gcd(A, B)
print(ans)