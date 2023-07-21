N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(input().split())

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in arr:
    print(student[0])