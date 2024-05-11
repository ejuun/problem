def d(n):
    val = 0
    temp = n
    for i in range(len(str(n))):
        div = temp % 10
        temp = temp // 10
        val += div
    return val + n

self = [0 for _ in range(20000)]
for i in range(1, 10001):
    self[d(i)] += 1

for i in range(1, 10001):
    if not self[i]:
        print(i)