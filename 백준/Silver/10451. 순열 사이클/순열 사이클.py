from collections import deque
for _ in range(int(input())):
    N = int(input())

    end = list(map(int, input().split()))
    visit = [False for _ in range(N)]
    ans = 0
    for i in range(N):
        if not visit[i]:
            ans += 1
            queue = deque()
            queue.append(i)
            visit[i] = True

            while queue:
                x = queue.popleft()
                if not visit[end[x]-1]:
                    visit[end[x]-1] = True
                    queue.append(end[x]-1)

    print(ans)