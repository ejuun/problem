m = 0
ans = ''
for _ in range(7):
    name, num = map(str, input().split())
    if int(num) > m:
        m = int(num)
        ans = name
print(ans)