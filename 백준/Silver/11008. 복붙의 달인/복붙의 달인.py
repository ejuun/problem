for _ in range(int(input())):
    p, s = map(str, input().split())
    ans = p.replace(s, "1")
    print(len(ans))