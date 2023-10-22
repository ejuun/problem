while 1:
    try:
        N, M = map(int, input().split())
        cnt = 0
        for i in range(N, M+1):
            num = str(i)
            num_list = list(num)
            num_set = set(num_list)
            if len(num_set) == len(num_list):
                cnt += 1
        print(cnt)
    except EOFError:
        break