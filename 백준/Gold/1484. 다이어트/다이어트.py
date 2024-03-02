G = int(input())

end = 1
diff = 0
ans = []
for start in range(1, 50002):
    diff = (end ** 2) - (start ** 2)

    while end <= 50002 and diff < G:
        end += 1
        diff = (end ** 2) - (start ** 2)

    if G == diff:
       ans.append(end)

if len(ans) == 0:
    print(-1)
else:
    for answer in ans:
        print(answer)