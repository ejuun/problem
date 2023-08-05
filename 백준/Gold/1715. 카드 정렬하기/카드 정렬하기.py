from heapq import heappush, heappop

N = int(input())
arr = []
for i in range(N):
    card = int(input())
    heappush(arr, card)

if N == 1:
    print(0)
else:
    ans = 0
    while len(arr) != 1:
        card1 = heappop(arr)
        card2 = heappop(arr)
        new_card = card1 + card2
        ans += new_card
        heappush(arr, new_card)
    print(ans)