word = list(input())
check = [0] * len(word)
able = ['.']
cnt = set()

def back(N):

    if len(able) == len(word)+1:
        cnt.add(''.join(able))
        return

    for i in range(len(check)):
        if not check[i] and able[-1] != word[i] :
            check[i] = 1
            able.append(word[i])
            back(N+1)
            able.pop()
            check[i] = 0

back(0)
print(len(cnt))