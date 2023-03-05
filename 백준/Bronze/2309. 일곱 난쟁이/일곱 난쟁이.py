small = []
for _ in range(9):
    height = int(input())
    small.append(height)

height_sum = sum(small)

for i in range(9):
    for j in range(i+1, 9):
        if height_sum - (small[i]+ small[j]) == 100:
            small.pop(j)
            small.pop(i)
            break
    if len(small) == 7:
        break

small.sort()
for s in small:
    print(s)