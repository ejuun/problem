arr = list(map(str, input()))
cnt = 0
stack = []
for i in range(len(arr)-1):
    if arr[i] == "(" and arr[i+1] == ")":
        cnt += len(stack)
    elif arr[i] == "(" and arr[i+1] != ")":
        stack.append(arr[i])
    elif arr[i] == ")" and arr[i+1] == "(":
        pass
    else:
        cnt += 1
        stack.pop()
print(cnt)