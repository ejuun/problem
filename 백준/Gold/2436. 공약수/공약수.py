def div(a,b):
    if a == 1 and b == 1:
        return 1

    for i in range(2, min(a, b)):
        if a % i == 0 and b % i == 0:
            return 0
    return 1

G, L = map(int, input().split())

ab = L // G
diff = L
A = B = 0

for a in range(1, ab//2+2):
    if not ab % a:
        b = ab // a
        if div(a, b) and diff > abs(b-a):
            diff = b-a
            A = a
            B = b

print(A*G, B*G)