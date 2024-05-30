import math
lst = list(input())

for i in range(len(lst)):
    if lst[i] == ':':
        n = int(''.join(lst[:i]))
        m = int(''.join(lst[i+1:]))
        break
        
gcd = math.gcd(n, m)
ans = [str(n//gcd), ":", str(m//gcd)]
print(''.join(ans))