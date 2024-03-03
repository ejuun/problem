A, B = map(int, input().split())

def f(num):
    hap = 0

    if num == 0:
        return hap

    cnt = 1
    if num % 2:
        hap += (((num+1) // 2) + ((num-1) // 2 * 2))
        while (num-1) // (2 ** cnt) > 0:
            hap += ((num-1) // 2 ** (cnt+1)) * (2**cnt)
            cnt += 1
    else:
        hap += ((num // 2) + ((num // 2) * 2))
        while num // (2 ** cnt) > 0:
            hap += (num // 2 ** (cnt + 1)) * (2**cnt)
            cnt += 1

    return hap

ans = f(B) - f(A-1)
print(ans)