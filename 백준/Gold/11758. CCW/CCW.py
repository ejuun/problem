x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def CCW(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

ans = CCW(x1, y1, x2, y2, x3, y3)
if ans > 0 :
    ans = 1
elif ans < 0:
    ans = -1
else:
    ans = 0
print(ans)