import sys
input = sys.stdin.readline

trees = dict()
cnt = 0
while True:
    tree = input().rstrip()
    if tree:
        cnt += 1
        if tree not in trees:
            trees[tree] = 1
        else:
            trees[tree] += 1
    else:
        break

new_tree = sorted(trees.items())
for t, n in new_tree:
    print(t, '{0:.4f}'.format(n/cnt * 100))