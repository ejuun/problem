num_list = list(input())
num_list.sort(reverse=True)
hap = 0
for i in range(len(num_list)):
    hap += int(num_list[i])

if int(num_list[-1]) != 0 or hap % 3:
    print(-1)
else:
    print(''.join(num_list))