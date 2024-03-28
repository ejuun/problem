N, K = map(int, input().split())
number = list(input())
ans = []
cnt = K
for num in number:

    while ans and 0 < cnt:
        if ans[-1] < num:
            ans.pop()
            cnt -= 1
        else:
            break
    ans.append(num)

print(''.join(ans[:N-K]))