import sys
input = sys.stdin.readline

N = int(input())
buildings = []
for _ in range(N):
    buildings.append(int(input()))
    
stack = []
result = 0

for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    stack.append(building)

    result += len(stack) - 1

print(result)