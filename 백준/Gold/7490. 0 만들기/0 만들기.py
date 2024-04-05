sign = [' ', '+', '-']

def back(n):
    if n == N:
        able = ''
        for i in range(len(test)):
            if test[i] != ' ':
                able += test[i]
        if eval(able) == 0:
            print(''.join(test))
        return

    for s in sign:
        test.append(s)
        test.append(str(n + 1))
        back(n + 1)
        test.pop()
        test.pop()

T = int(input())
for _ in range(T):
    N = int(input())
    test = ['1']
    back(1)
    print()