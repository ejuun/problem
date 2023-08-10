N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e10
min_val = 1e10

def back(i, now):
    global add, sub, mul, div, max_val, min_val

    if i == N:
        max_val = max(max_val, now)
        min_val = min(min_val, now)
        return

    else:
        if add > 0:
            add -= 1
            back(i + 1, now + arr[i])
            add += 1
        if sub > 0:
            sub -= 1
            back(i + 1, now - arr[i])
            sub += 1
        if mul > 0:
            mul -= 1
            back(i + 1, now * arr[i])
            mul += 1
        if div > 0:
            div -= 1
            back(i + 1, int(now / arr[i]))
            div += 1

back(1, arr[0])

print(max_val)
print(min_val)