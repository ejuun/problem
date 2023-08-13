num = int(input())
cnt = [0] * 10
for i in str(num):
    if i == '6' or i == '9':
        if cnt[6] == cnt[9]:
            cnt[6] += 1
        else:
            cnt[9] += 1
    else:
        cnt[int(i)] += 1
print(max(cnt))
