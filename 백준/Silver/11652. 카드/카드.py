card = {}
for _ in range(int(input())):
    n = int(input())
    if n not in card:
        card[n] = 1
    else:
        card[n] += 1

lst = []
for key, value in card.items():
    lst.append((key, value))
lst.sort(key=lambda x: (-x[1], x[0]))
print(lst[0][0])