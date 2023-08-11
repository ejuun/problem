N = int(input())
arr = list(map(int ,input().split()))
ans = 0

def back(arr, new_N, hap):

    global ans

    if new_N == 2:
        if ans < hap:
            ans = hap
            return
        return

    for i in range(1, new_N-1):
        copyarr = arr[:]
        newHap = arr[i-1] * arr[i+1]
        arr.pop(i)
        back(arr, new_N-1, hap + newHap)
        arr = copyarr[:]

back(arr, N, 0)
print(ans)