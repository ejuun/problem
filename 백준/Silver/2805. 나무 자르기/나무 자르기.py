N, M = map(int, input().split())
trees = list(map(int, input().split()))
low = 1
high = max(trees)

ans = 0
while low <= high:
    mid = (high+low) // 2

    able = 0
    for tree in trees:
        if tree > mid:
            able += tree - mid

    if able == M:
        ans = mid
        break
    else:
        if able > M:
            low = mid + 1
            if ans < mid:
                ans = mid
        else:
            high = mid - 1
print(ans)