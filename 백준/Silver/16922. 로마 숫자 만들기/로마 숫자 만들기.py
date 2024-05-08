from itertools import combinations_with_replacement
roma = [1, 5, 10, 50]
N = int(input())
lst = combinations_with_replacement(roma, N)
ans = set()
for able in lst:
    ans.add(sum(able))
print(len(ans))