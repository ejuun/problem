N = int(input())
arr = []
ans = 0
arr_set = set()
def back(n):
    global ans
    if n == N:
        if sum(arr) > 0 and sum(arr) % 3 == 0:
            s_arr = tuple(sorted(arr))
            z, o, t = 0, 0, 0
            if not s_arr in arr_set:
                arr_set.add(s_arr)
                for number in arr:
                    if number == 0:
                        z += 1
                    elif number == 1:
                        o += 1
                    elif number == 2:
                        t += 1
                val = int(fac(N) / (fac(z) * fac(o) * fac(t)))
                if z:
                    val -= int(fac(N-1) / (fac(z-1) * fac(o) * fac(t)))
                ans += val
                return
        return
    for i in range(3):
        arr.append(i)
        back(n+1)
        arr.pop()

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)

back(0)
print(ans)