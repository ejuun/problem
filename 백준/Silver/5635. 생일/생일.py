n = int(input())
lst = []
for _ in range(n):
    n, d, m, y = input().split()
    d, m, y = map(int, (d, m, y))
    lst.append((y, m, d, n))
lst.sort()
print(lst[-1][-1])
print(lst[0][-1])
