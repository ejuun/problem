f = [i for i in range(21)]
for i in range(2, 21):
    f[i] = f[i-2] + f[i-1]
n = int(input())
print(f[n])