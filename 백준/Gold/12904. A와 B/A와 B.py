S = input()
T = input()

while 1:
    if T[len(T)-1] == 'A':
        T = T[:len(T)-1]
    elif T[len(T)-1] == 'B':
        T = T[:len(T)-1]
        T = T[::-1]

    if len(T) == len(S):
        if T != S:
            print(0)
            break
        else:
            print(1)
            break