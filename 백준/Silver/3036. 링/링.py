import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
arr = list(map(int, input().split()))
for i in range(1, N):
    m = arr[0] // gcd(arr[0], arr[i])
    c = arr[i] // gcd(arr[0], arr[i])
    print(f'{m}/{c}')