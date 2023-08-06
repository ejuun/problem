N = int(input())

lst = [0] * N
for i in range(N):
    lst[i] = int(input())

lst.sort()

for i in range(N-1, -1, -1):
    print(lst[i])