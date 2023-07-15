import math
N = int(input())
arr = [1] * (N+1)
for i in range(2, int(math.sqrt(N))+1):
    if arr[i]:
        for j in range(2*i, N+1, i):
            arr[j] = 0
            
prime = []
for i in range(2, len(arr)):
    if arr[i]:
        prime.append(i)
        
end = ans = hap = 0
for start in range(len(prime)):

    while hap < N and end < len(prime):
        hap += prime[end]
        end += 1

    if hap == N:
        ans += 1
    hap -= prime[start]

print(ans)