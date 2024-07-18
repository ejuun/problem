arr = [list(map(int, input().split())) for _ in range(3)]
D = (arr[1][0] - arr[0][0])*(arr[2][1] - arr[0][1]) - (arr[1][1] - arr[0][1])*(arr[2][0] - arr[0][0])

if D == 0:
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')