n = input()

arr = [0] * len(n)

for i in range(len(n)):
    arr[i] = n[i]

new_arr = sorted(arr, reverse= True)

ans =''

for num in new_arr:
    ans += num

print(ans)