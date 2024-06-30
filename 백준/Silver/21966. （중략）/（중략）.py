import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()
if N <= 25:
    print(S)
elif N > 25:
    if "." in S[11:-12]:
        print(S[:9] + "......" + S[-10:])
    else:
        print(S[:11] + "..." + S[-11:])