cnt = 1
while 1:
    N = int(input())
    if not N:
        break

    arr = []
    for _ in range(N):
        arr.append(input())

    arr.sort()
    print(cnt)
    for lst in arr:
        print(lst)

    cnt += 1