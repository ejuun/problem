import math
import sys
input = sys.stdin.readline

m = 1000001
num = [True for _ in range(m)]
for i in range(2, int(math.sqrt(m))+1):
    if num[i] == True:
        for j in range(i*2, m, i):
            num[j] = False

prime = set()
for i in range(3, m):
    if num[i]:
        prime.add(i)

while 1:
    n = int(input())
    if not n:
        break

    ans = "Goldbach's conjecture is wrong."
    for i in range(3, m, 2):
        if num[i]:
            temp = n - i
            if temp in prime:
                ans = "{} = {} + {}".format(n, i, temp)
                break
    print(ans)