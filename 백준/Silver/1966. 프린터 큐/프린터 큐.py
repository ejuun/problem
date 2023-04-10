from collections import deque
for tc in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    check_list = [0] * N
    check_list[M] = 1

    check_queue = deque()
    for num in check_list:
        check_queue.append(num)

    queue = deque()
    for num in lst:
        queue.append(num)
    def check(M):
        cnt = 0
        while 1:
            max_val = 0
            for num in queue:
                if max_val <= num:
                    max_val = num
            while max_val in queue:
                while queue[0] != max_val:
                    a = queue.popleft()
                    b = check_queue.popleft()
                    queue.append(a)
                    check_queue.append(b)
                queue.popleft()
                ans = check_queue.popleft()
                if ans == 1:
                    return cnt
                cnt += 1
    print(check(M)+1)
