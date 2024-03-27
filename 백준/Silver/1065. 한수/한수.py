N = int(input())
if N < 100:
    print(N)
else:
    ans = 99
    num = [str(i) for i in range(100, N+1)]
    for number in num:
        if 2 * (int(number[0]) - int(number[1])) == int(number[0]) - int(number[2]):
            ans += 1
    print(ans)