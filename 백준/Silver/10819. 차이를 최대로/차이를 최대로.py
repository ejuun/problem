N = int(input())
num = list(map(int, input().split()))

arr = [i for i in range(N)]

max_val = 0

def perm(i, k):
    global max_val
    if i == k:
        hap = 0
        for a in range(1, len(arr)):
            hap += abs(num[arr[a-1]]-num[arr[a]])
        if max_val < hap:
            max_val = hap
            return
        return

    for j in range(i, k):
        arr[i], arr[j] = arr[j], arr[i]
        perm(i+1, k)
        arr[i], arr[j] = arr[j], arr[i]

perm(0, N)

print(max_val)