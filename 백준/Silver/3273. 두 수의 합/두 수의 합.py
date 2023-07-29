n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

end = n-1
start = 0
ans = 0
while start < end:
    hap = arr[start] + arr[end]

    if hap == x:
        ans +=1
        start += 1
        end -=1

    elif hap > x:
        end -= 1
    else:
        start += 1

print(ans)