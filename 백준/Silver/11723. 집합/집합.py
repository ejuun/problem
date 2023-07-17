import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    put = (sys.stdin.readline().strip().split())
    if put[0] == 'add':
        S.add(int(put[1]))
    elif put[0] == 'check':
        if int(put[1]) in S:
            print(1)
        else:
            print(0)
    elif put[0] == 'remove':
        S.discard(int(put[1]))
    elif put[0] == 'toggle':
        if int(put[1]) in S:
            S.remove(int(put[1]))
        else:
            S.add(int(put[1]))
    elif put[0] == 'all':
        S = set(range(1, 21))
    elif put[0] == 'empty':
        S = set()