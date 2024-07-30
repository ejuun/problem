import sys
input = sys.stdin.readline

stack = []
ans = 0
for _ in range(int(input())):
    hw = list(map(int, input().split()))

    if len(hw) == 3:
        if hw[2] == 1:
            ans += hw[1]
        else:
            hw[2] -= 1
            stack.append(hw)
    else:
        if not stack:
            continue
        else:
            last = stack.pop()
            if last[2] == 1:
                ans += last[1]
            else:
                last[2] -= 1
                stack.append(last)
print(ans)