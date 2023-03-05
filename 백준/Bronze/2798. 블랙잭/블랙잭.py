N, M = map(int, input().split())
card = list(map(int, input().split()))

max_sum = 0

for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            if card[i] + card[j] + card[k] <= M:
                if max_sum <= card[i] + card[j] + card[k]:
                    max_sum = card[i] + card[j] + card[k]
print(max_sum)