def solution(n, s):
    answer = []
    
    while s > n:
        temp = s // n
        answer.append(temp)
        s -= temp
        n -= 1
    
    if not len(answer):
        answer.append(-1)
    
    return answer