import sys
input =sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

price = arr[0]
earn = 0
for i in range(1, N):
    if earn < arr[i] - price:
        earn = arr[i] - price

    if price > arr[i]:
        price = arr[i]

print(earn)