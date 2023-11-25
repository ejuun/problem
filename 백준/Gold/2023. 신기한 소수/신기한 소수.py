import math
N = int(input())

def prime(num):
    for n in range(2, int(math.sqrt(num))+1):
        if not num % n:
            return 0
    return 1

def findNum(n):

    if len(str(n)) == N:
        print(n)
        return

    for i in range(1, 10):
        new_n = 10*n + i
        check = prime(new_n)
        if check:
            findNum(new_n)

findNum(2)
findNum(3)
findNum(5)
findNum(7)