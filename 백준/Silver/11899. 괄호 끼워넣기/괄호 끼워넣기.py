S = input()
open =[]
close = []
for s in S:
    if s == '(':
        open.append(s)
    else:
        if open:
            open.pop()
        else:
            close.append(s)

print(len(open) + len(close))