def anc_list(n, n_parent):
    n_parent.append(n)
    while n != p[n]:
        n_parent.append(p[n])
        n = p[n]
    return n_parent

def anc_set(n, n_parent):
    n_parent.add(n)
    while n != p[n]:
        n_parent.add(p[n])
        n = p[n]
    return n_parent

for _ in range(int(input())):
    N = int(input())

    p = [i for i in range(N + 1)]

    for _ in range(N - 1):
        parent, child = map(int, input().split())
        p[child] = parent

    q1, q2 = map(int, input().split())

    q1_parent = []
    q2_parent = set()

    q1_tree = anc_list(q1, q1_parent)
    q2_tree = anc_set(q2, q2_parent)

    for ans in q1_tree:
        if ans in q2_tree:
            break
    print(ans)