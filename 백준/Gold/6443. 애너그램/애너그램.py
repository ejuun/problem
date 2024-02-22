import sys
input = sys.stdin.readline

def back(word, answer):
    if len(answer) == len(word):
        print(''.join(answer))
        return

    for i in dic:
       if dic[i]:
           dic[i] -= 1
           answer.append(i)
           back(word, answer)
           answer.pop()
           dic[i] += 1

N = int(input())
for _ in range(N):
    words = sorted(input().rstrip())
    ans = []
    dic = dict()
    
    for alpha in words:
        if alpha in dic:
            dic[alpha] += 1
        else:
            dic[alpha] = 1
    
    back(''.join(words), ans)