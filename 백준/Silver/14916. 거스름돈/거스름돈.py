n = int(input())

if n < 5:
    if n == 2:
        print(1)
    elif n == 4:
        print(2)
    else:
        print(-1)
else:
    ans = -1
    q = n // 5
    for coin in range(q, -1, -1):
        div = n - coin * 5
        if not div % 2:
            ans = coin + div // 2
            break
    print(ans)