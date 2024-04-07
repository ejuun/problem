import sys
input = sys.stdin.readline
N = int(input())

rainbow = set()
rainbow.add('ChongChong')
for _ in range(N):
    A, B = map(str, input().rstrip().split())
    if A in rainbow:
        rainbow.add(B)
    if B in rainbow:
        rainbow.add(A)

print(len(rainbow))