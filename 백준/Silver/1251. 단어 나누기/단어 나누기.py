word = list(input())
able = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        f = word[:i]
        s = word[i:j]
        t = word[j:]
        f.reverse()
        s.reverse()
        t.reverse()
        able.append(''.join(f)+''.join(s)+''.join(t))
able.sort()
print(able[0])