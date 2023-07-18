def hap(n):
    sums = 0
    for i in range(n):
        sums += Catalan[i] * Catalan[(n-1)-i]
    return sums

Catalan = [0] * 31
Catalan[0] = Catalan[1] = 1
for i in range(2, 31):
    Catalan[i] = hap(i)

while 1:
    N = int(input())
    if not N :
        break
    print(Catalan[N])