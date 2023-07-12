T = int(input())

for _ in range(T):
     
    N = int(input())
    lst = list(map(str, input().split()))
    ans = 100000

    if N < 33:

        min_gap = 100000
        for i in range(len(lst)-2):
            for j in range(i+1, len(lst)-1):
                for k in range(j+1, len(lst)):
                    # print(lst[i], lst[j], lst[k])
                    gap = 0
                    for l in range(4):
                        if lst[i][l]!= lst[j][l]:
                            gap += 1
                        if lst[i][l]!= lst[k][l]:
                            gap += 1
                        if lst[j][l]!= lst[k][l]:
                            gap += 1

                    if min_gap > gap:
                        min_gap = gap
        ans = min_gap
    else:
        ans = 0

    print(ans)