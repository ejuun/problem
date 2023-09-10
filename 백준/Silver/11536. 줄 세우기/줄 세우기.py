N = int(input())
name = [0] * N
for i in range(N):
    name[i] = input()

increase_name = sorted(name)
decrease_name = sorted(name, key= lambda x : x, reverse=True)

if name == increase_name:
    print('INCREASING')
elif name == decrease_name:
    print('DECREASING')
else:
    print("NEITHER")