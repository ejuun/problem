arr = [i for i in range(10001)]
for i in range(6, 10001):
    arr[i] = arr[i-3] + (arr[i-2] - arr[i-5]) + 1
for _ in range(int(input())):
    print(arr[int(input())])