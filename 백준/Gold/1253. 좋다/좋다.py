import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

if N == 1:
    print(0)
else:
    cnt = order = 0

    while order < N:
        start = 0
        end = N-1

        while start < end:
            if start == order:
                start += 1
                continue
            elif end == order:
                end -= 1
                continue

            hap = arr[start] + arr[end]
            if hap < arr[order]:
                start += 1
            elif hap > arr[order]:
                end -= 1
            else:
                cnt += 1
                break

        order += 1

    print(cnt)