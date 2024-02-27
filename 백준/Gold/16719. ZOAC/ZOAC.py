word = list(input())

use = [''] * len(word)

while 1:
    able = []
    for i in range(len(word)):
        if use[i] == '':
            use[i] = word[i]
            able.append((''.join(use), i))
            use[i] = ''
    able.sort()
    use[able[0][1]] = word[able[0][1]]
    print(able[0][0])
    if ''.join(use) == ''.join(word):
        break